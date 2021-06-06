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

    return errors

   # avgError = mean(errors)
   # return avgError, errors


def testMore(subsetNumber, model, testNumber):
    attributes = list(range(54))

    avgErrors = []

    # aggregate errors from several tests
    for i in range (0, testNumber):
        dataset = ImportData.convert()
        errors = crossValidation(dataset, subsetNumber, attributes, model)
        if len(avgErrors) == 0:
            avgErrors = errors
        else:
            for j in range(len(avgErrors)):
                avgErrors[j] += errors[j]

    for i in range(len(avgErrors)):
        avgErrors[i] = avgErrors[i]/testNumber

    avgError = mean(avgErrors)

    modelName = None
    if model == ID3:
        modelName = "ID3"
    else:
        if model == C45:
            modelName = "C45"
        else:
            raise Exception("model type is not in {ID3, C45}")

    print(modelName)
    avgError = float("{:.3f}".format(avgError))
    print("avg error : " + str(avgError))

    for i in range(len(avgErrors)):
        avgErrors[i] = float("{:.3f}".format(avgErrors[i]))

    print("errors : " + str(avgErrors) + "\n")
