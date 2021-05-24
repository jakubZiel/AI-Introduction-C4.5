import math
import pandas as pd

def mostFreqClass(dataset):
    valueFreq = {}
    classIndex = len(dataset)-1;
    mostFreq = 0
    mostFreqClass = ""

    for row in dataset:
        if (valueFreq.has_key(row[classIndex])):
            valueFreq[row[classIndex]] += 1
        else:
            valueFreq[row[classIndex]] = 1

    for c in valueFreq.keys():
        if valueFreq[c] > mostFreq:
            mostFreq = valueFreq[c]
            mostFreqClass = c

    return mostFreqClass

def bestAttribute(attributes, dataset):
    best = attributes[0]
    maxInfGain = 0

    for attr in attributes:
        currInfGain = calculateInfGain(attr, attributes, dataset)
        if currInfGain > maxInfGain:
            maxInfGain = currInfGain
            best = attr
    return best

def calculateEntropy(attrIndex, dataset):
    valueFreq = {}
    entropy = 0.0

    for row in dataset:
        if row[attrIndex] in valueFreq.keys():
            valueFreq[row[attrIndex]] += 1
        else:
            valueFreq[row[attrIndex]] = 1

    for f in valueFreq.values():
        fi = f/len(dataset)
        entropy -= fi*math.log(fi, math.e)

    return entropy


def calculateInfGain(attr, attributes, dataset):

    #calculate entire dataset entropy - using classes frequency
    classIndex = len(attributes)-1 #assuming class as last attribute
    datasetEntropy = calculateEntropy(classIndex, dataset)

    #calculate subsets' entropies
    attrIndex = dataset.index(attr)

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
        subset = split_data(attrIndex, a, dataset)
        attrEntropy += attrValueFreq[a] / len(dataset) * calculateEntropy(attrIndex, subset)

    return datasetEntropy - attrEntropy


def split_data(attrIndex, attrVal, dataset):
    newDataset = []

    for row in dataset:
        if row[attrIndex] == attrVal:
            subset = list(row[:attrIndex])
            subset.extend(row[attrIndex+1:])
            newDataset += subset

    return newDataset


def ID3(attributes, dataset, recursionLevel):
    recursionLevel += 1

    #same class in all cases, put it into leaf
    classes = [row[-1] for row in dataset]
    if classes.count(classes[0]) == len(classes):
        return classes[0];

    #no more attributes -> get most frequent class
    if (len(attributes) - 1) <= 0:
        return mostFreqClass(dataset)

    #d - attribute with highest InfGain
    d = bestAttribute(attributes, dataset)
    Tree = {d:{}}

    #preparing attribute parameters for children nodes
    attrValues = [row[d] for row in dataset]
    attrValues = set(attrValues)
    attrIndex = dataset.index(d)
    del(attributes[attrIndex])

    #children nodes
    for attrVal in attrValues:
        subAttr = attributes[:]
        Tree[d][attrVal] = ID3(attributes, split_data(attrIndex, attrVal, dataset), recursionLevel)

    return Tree

def test1():
    outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
    temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
    humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
    windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
    play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')

    dataset ={'outlook':outlook,'temp':temp,'humidity':humidity,'windy':windy,'play':play}
    df = pd.DataFrame(dataset, columns=dataset.keys())

    print(df)

    attr = list(df.columns)
    print(attr)

  #  tree = ID3(attr, dataset, 0)
