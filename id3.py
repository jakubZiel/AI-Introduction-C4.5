import math
import pandas as pd
import DecisionNode

def mostFreqClass(dataset):
    valueFreq = {}
    classes = dataset[-1]

    for row in dataset:
        c = row[-1]
        if c in valueFreq.keys():
            valueFreq[c] += 1
        else:
            valueFreq[c] = 1

    mfc = ""
    maxFreq = 0

    for k in valueFreq.keys():
        if valueFreq[k]>maxFreq:
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
     #   print("cura: ", attr, "curBest: ", best, "curIG: ", currInfGain)
    return best

#
# def calculateEntropy(attrIndex, dataset):
#     valueFreq = {}
#     entropy = 0.0
#
#     for row in dataset:
#         if row[attrIndex] in valueFreq.keys():
#             valueFreq[row[attrIndex]] += 1
#         else:
#             valueFreq[row[attrIndex]] = 1
#
#     for f in valueFreq.values():
#         fi = f/len(dataset)
#         entropy -= fi*math.log(fi, math.e)
#
#     return entropy

def calculateEntropy2(dataset):
    valueFreq = {}
    entropy = 0.0

    for row in dataset:
        if row[-1] in valueFreq.keys():
            valueFreq[row[-1]] += 1
        else:
            valueFreq[row[-1]] = 1

    for f in valueFreq.values():
        fi = f/len(dataset)
        entropy -= fi*math.log(fi, math.e)

    return entropy


def calculateInfGain(attrIndex, dataset):

    #calculate entire dataset entropy - using classes frequency
    datasetEntropy = calculateEntropy2(dataset)
   # print(datasetEntropy)

    #calculate subsets' entropies
    attrValueFreq = {}
    attrEntropy = 0.0

    #looking for attribute values
    for row in dataset:
        if row[attrIndex] in attrValueFreq.keys():
            attrValueFreq[row[attrIndex]] += 1
        else:
            attrValueFreq[row[attrIndex]] = 1

   # print(attrValueFreq)

    #splittling into subsets by attribute values
    for a in attrValueFreq.keys():
        subset = splitForEntropy(attrIndex, a, dataset)
        # print("a: ", a)
        # print("subset: ", subset)
        attrEntropy += float(attrValueFreq[a] / len(dataset) * calculateEntropy2(subset))
        # print(len(subset))
        # print(attrEntropy)

    return datasetEntropy - attrEntropy


def splitForEntropy(attrIndex, attrVal, dataset):
    newDataset = []

    for row in dataset:
        if row[attrIndex] == attrVal:
            subset = row
            newDataset.append(subset)

    return newDataset


def split_data(attrIndex, attrVal, dataset):
    newDataset = []

    for row in dataset:
        if row[attrIndex] == attrVal:
            subset = row[:attrIndex] + row[attrIndex+1:]
            newDataset.append(subset)

    return newDataset


def ID3(classes, attributes, dataset, recursionLevel, parentNode):
    recursionLevel += 1

    #same class in all cases, put it into leaf
    if classes.count(classes[0]) == len(classes):
        c = classes[0][0]
        return DecisionNode.DecisionNode(None, c, parentNode)

    #no more attributes -> get most frequent class
    if (len(attributes) - 1) <= 0:
        mfc = mostFreqClass(dataset)
        return DecisionNode.DecisionNode(None, mfc, parentNode)

    #d - attribute with highest InfGain
    d = bestAttribute(attributes, dataset)
    Tree = DecisionNode.DecisionNode(d, None, parentNode)

    #preparing attribute parameters for children nodes
    attrValues = [row[d] for row in dataset]
    attrValues = set(attrValues)
    attrIndex = d
    del(attributes[d])

    # tested until here

    #children nodes
    for attrVal in attrValues:
        subAttr = attributes[:]
        Tree.children[attrVal] = ID3(classes, attributes, split_data(attrIndex, attrVal, dataset), recursionLevel, Tree)

    return Tree

def test1():

    dataset = [[2, 1, 3, 4], [1, 1, 2, 4], [1, 3, 3, 4], [4, 3, 4, 0]]
    dataset2 = [[1,1,0], [2,1,1], [2,2,1], [2,2,0], [2,3,1]]
    attr = [0, 1]
    classes2 = [0, 0, 1, 1]
    classes = [[0], [1], [1], [0], [1]]

    print(mostFreqClass(dataset2))
    #
    # d = bestAttribute(classes, attr, dataset2)
    # print("best: ", d)
    #
    # attrValues = [row[d] for row in dataset2]
    # attrValues = set(attrValues)
    #
    # print(attrValues)
    # print(attr[d])

#    print(bestAttribute(attr, dataset))
#    print(calculateEntropy2(dataset[0]))
#     print(calculateInfGain(classes, 0, dataset2))


    tree = ID3(classes, attr, dataset, 0, None)
