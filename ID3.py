import math

from DecisionNode import DecisionNode


def mostFreqClass(dataset):
    valueFreq = {}

    for row in dataset:
        c = row[-1]
        if c in valueFreq.keys():
            valueFreq[c] += 1
        else:
            valueFreq[c] = 1

    mfc = ""
    maxFreq = 0

    for k in valueFreq.keys():
        if valueFreq[k] > maxFreq:
            maxFreq = valueFreq[k]
            mfc = k

    return mfc


def bestAttribute(attributes, dataset):
    best = attributes[0]
    maxInfGain = 0

    for attr in attributes:
        currInfGain = calculateInfGain(attr, dataset)
        if currInfGain > maxInfGain:
            maxInfGain = currInfGain
            best = attr

    return best


def calculateEntropy2(dataset):
    valueFreq = {}
    entropy = 0.0

    for row in dataset:
        if row[-1] in valueFreq.keys():
            valueFreq[row[-1]] += 1
        else:
            valueFreq[row[-1]] = 1

    for f in valueFreq.values():
        fi = f / len(dataset)
        entropy -= fi * math.log(fi, math.e)

    return entropy


def calculateInfGain(attrIndex, dataset):
    # calculate entire dataset entropy - using classes frequency
    datasetEntropy = calculateEntropy2(dataset)

    # calculate subsets' entropies
    attrValueFreq = {}
    attrEntropy = 0.0

    # looking for attribute values
    for row in dataset:
        if row[attrIndex] in attrValueFreq.keys():
            attrValueFreq[row[attrIndex]] += 1
        else:
            attrValueFreq[row[attrIndex]] = 1

    # splittling into subsets by attribute values
    for a in attrValueFreq.keys():
        subset = splitForEntropy(attrIndex, a, dataset)
        attrEntropy += float(attrValueFreq[a] / len(dataset) * calculateEntropy2(subset))

    return datasetEntropy - attrEntropy


def splitForEntropy(attrIndex, attrVal, dataset):
    newDataset = []

    for row in dataset:
        if row[attrIndex] == attrVal:
            subset = row
            newDataset.append(subset)

    return newDataset


def dataset_slice(attrIndex, attrVal, dataset):
    newDataset = []

    for record in dataset:
        if record[attrIndex] == attrVal:
            newDataset.append(record)

    return newDataset


def ID3(attributes: list, dataset: list, parentDecision: int, parentNode: DecisionNode):
    classes = []
    for record in dataset:
        classes.append(record[-1])

    if classes.count(classes[0]) == len(classes):
        return DecisionNode.createLeaf(classes[0], parentDecision, parentNode)

    if len(attributes) == 0:
        majorityClass = mostFreqClass(dataset)
        return DecisionNode.createLeaf(majorityClass, parentDecision, parentNode)

    bestSplitAttribute = bestAttribute(attributes, dataset)
    attributes.remove(bestSplitAttribute)

    decisionNode = DecisionNode.createDecision(bestSplitAttribute, parentDecision, parentNode)

    attributeValues = set()

    for record in dataset:
        attrVal = record[bestSplitAttribute]
        attributeValues.add(attrVal)

    for val in attributeValues:
        subDataSet = dataset_slice(bestSplitAttribute, val, dataset)
        decisionNode.children[val] = ID3(attributes, subDataSet, val, decisionNode)

    return decisionNode


def predict(root: DecisionNode, attributeValues):
    if root.isLeaf:
        return root.classValue

    decisionAttr = root.attributeNumber

    currAttrValue = attributeValues[decisionAttr]

    return predict(root.children[currAttrValue], attributeValues)


def test1():
    dataset = [[2, 1, 3, 1], [1, 1, 2, 0], [1, 3, 3, 1], [4, 3, 4, 0]]
    dataset2 = [[1, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 1]]

    attributes = [0, 1, 2]
    attributes2 = [0, 1]

    root = ID3(attributes2, dataset2, None, None)

    print()
