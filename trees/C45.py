from DecisionNode import DecisionNode
from trees.ID3 import ID3, predict
from utilities import ImportData
import math


def traverseLeaves(root: DecisionNode, frequencies: list):
    if root is None:
        return
    if root.isLeaf:
        if root.classValue == 0:
            frequencies[0] += 1
        else:
            frequencies[1] += 1
        return

    for child in root.children:
        traverseLeaves(child, frequencies)


def mostFrequentInTree(root: DecisionNode):
    frequencies = [0, 0]

    traverseLeaves(root, frequencies)

    return 0 if frequencies[0] > frequencies[1] else 1


def traverse(root: DecisionNode, leaves: list):
    if root is None:
        return
    if root.isLeaf:
        leaves.append(root)
        return

    for child in root.children:
        traverse(child, leaves)


def findLeaves(root: DecisionNode):
    leaves = []
    traverse(root, leaves)
    return leaves


def testError(root: DecisionNode, teachingSet: list, datasetSize: int):
    missed = 0

    for record in teachingSet:
        if predict(root, record[:-1]) != record[-1]:
            missed += 1

    teachingSetError = float(missed) / float(len(teachingSet))

    testSetEstimatedError = teachingSetError + math.sqrt(teachingSetError * (1 - teachingSetError)) / datasetSize

    return testSetEstimatedError


def pruneNode(node: DecisionNode, classVal, leaves: list):
    if node is None:
        raise Exception("pruning None")
    if node.isLeaf:
        raise Exception("pruning leaf")

    node.isLeaf = True
    node.classValue = classVal
    node.attributeNumber = None

    for i in range(5):
        try:
            leaves.remove(node.children[i])
            node.children[i] = None
        except ValueError:
            pass


def checkPath(root: DecisionNode, leaf: DecisionNode, teachingSet: list, leaves: list, datasetSize: int):
    node = leaf.parent

    while node is not None:

        mostFrequentClass = mostFrequentInTree(node)
        substitute = DecisionNode.createLeaf(mostFrequentClass, node.decisionValue, node.parent)

        error0 = testError(node, teachingSet, datasetSize)
        error1 = testError(substitute, teachingSet, datasetSize)

        if error0 >= error1:
            pruneNode(node, mostFrequentClass, leaves)

        node = node.parent


def C45(attributes: list, teachingSet: list, datasetSize):
    root = ID3(attributes, teachingSet, None, None)

    leaves = findLeaves(root)
    for leaf in leaves:
        if leaf is not None:
            checkPath(root, leaf, teachingSet, leaves, datasetSize)

    return root


def test():
    attributes = list(range(54))

    output = ImportData.convert("data/divorce.csv")

    teachingSetSize = int(len(output) * 0.8)

    teachingSet = output[:teachingSetSize]
    testingSet = output[teachingSetSize:]
    datasetSize = len(output)

    root = C45(attributes.copy(), teachingSet, datasetSize)

    errors = 0

    for record in testingSet:
        if predict(root, record[:-1]) != record[-1]:
            errors += 1

    print(errors / len(testingSet))

    return root
