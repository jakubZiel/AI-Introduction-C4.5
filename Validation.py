from trees.ID3 import *
from statistics import mean
from utilities import ImportData
from trees.C45 import *


def split(dataset: list, subsetNumber: int):
    subsets = []
    subsetSize = int(len(dataset) / subsetNumber)

    for j in range(subsetNumber):
        subset = []
        for i in range(subsetSize):
            index = random.randint(0, len(dataset) - 1)
            subset.append(dataset.pop(index))

        subsets.append(subset)

    return subsets


def listsToList(subsets: list):
    output = []

    for subset in subsets:
        for record in subset:
            output.append(record)

    return output


def crossValidation(dataset: list, subsetNumber: int, attributes: list, model):
    subsets = split(dataset, subsetNumber)
    errors = []

    for i in range(len(subsets)):
        error = 0

        testingSet = subsets[i]

        teachingSet = subsets[:i] + subsets[i + 1:]
        teachingSet = listsToList(teachingSet)

        if model == ID3:
            root = model(attributes.copy(), teachingSet, None, None)
        else:
            if model == C45:
                teachingSetSize = len(teachingSet)
                buildingSetSize = int(teachingSetSize * 0.8)

                buildingSet = teachingSet[:buildingSetSize]
                pruningSet = teachingSet[buildingSetSize:]

                root = model(attributes.copy(), buildingSet, pruningSet)
            else:
                raise Exception("model type is not in {ID3, C45}")

        for record in testingSet:
            if predict(root, record[:-1]) != record[-1]:
                error += 1

        error = error / len(testingSet)
        errors.append(error)

    avgError = mean(errors)

    return avgError, errors


def small_test():
    dataset2 = [[1, 1, 2, 0, 1], [2, 1, 4, 1, 1], [2, 2, 2, 2, 0], [2, 2, 0, 3, 1], [2, 3, 1, 4, 1],
                [1, 4, 0, 2, 1], [1, 1, 4, 3, 0], [1, 1, 1, 4, 1], [3, 1, 0, 1, 1], [4, 3, 0, 0, 0],
                [3, 2, 1, 4, 0], [4, 0, 2, 3, 1], [3, 4, 3, 2, 0], [4, 0, 4, 1, 0], [1, 2, 4, 0, 1]]

    attributes2 = [0, 1, 2, 3]

    crossValidation(dataset2, 3, attributes2, ID3)


# can't be 1
def test(subsetNumber, model):
    attributes = list(range(54))

    dataset = ImportData.convert()

    error, errors = crossValidation(dataset, subsetNumber, attributes, model)

    modelName = None
    if model == ID3:
        modelName = "ID3"
    else:
        if model == C45:
            modelName = "C45"
        else:
            raise Exception("model type is not in {ID3, C45}")

    print(modelName)
    error = float("{:.3f}".format(error))
    print("avg error : " + str(error))

    for i in range(len(errors)):
        errors[i] = float("{:.3f}".format(errors[i]))

    print("errors : " + str(errors) + "\n")
