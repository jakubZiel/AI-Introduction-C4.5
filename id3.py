import math
import DecisionNode

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
        fi = f/len(dataset)
        entropy -= fi*math.log(fi, math.e)

    return entropy


def calculateInfGain(attrIndex, dataset):

    #calculate entire dataset entropy - using classes frequency
    datasetEntropy = calculateEntropy2(dataset)

    #calculate subsets' entropies
    attrValueFreq = {}
    attrEntropy = 0.0

    #looking for attribute values
    for row in dataset:
        if row[attrIndex] in attrValueFreq.keys():
            attrValueFreq[row[attrIndex]] += 1
        else:
            attrValueFreq[row[attrIndex]] = 1

    #splittling into subsets by attribute values
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


def split_data(attrIndex, attrVal, dataset):
    newDataset = []

    for row in dataset:
        if row[attrIndex] == attrVal:
            subset = row[:attrIndex] + row[attrIndex+1:]
            newDataset.append(subset)

    return newDataset


def ID3(attributes, dataset, recursionLevel, parentNode):
    recursionLevel += 1

    #same class in all cases, put it into leaf
    #prepare classes from current dataset
    classes =[]
    for row in dataset:
#        print(row)
        classes.append(row[-1])

#    print(classes)
    if classes.count(classes[0]) == len(classes):
        c = classes[0]
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

    # well tested until here

    #children nodes
    for attrVal in attrValues:
        subAttr = attributes[:]
        Tree.children[attrVal] = ID3(subAttr, split_data(attrIndex, attrVal, dataset), recursionLevel, Tree)

    return Tree

def test1():

    dataset = [[2, 1, 3, 4], [1, 1, 2, 4], [1, 3, 3, 4], [4, 3, 4, 0]]
    dataset2 = [[1,1,0], [2,1,1], [2,2,1], [2,2,0], [2,3,1]]
    attr = [0, 1]

    tree = ID3(attr, dataset2, 0, None)
