from DecisionNode import DecisionNode
from ID3 import ID3, predict


def traverse(root: DecisionNode, leaves: list):
    if root.isLeaf:
        leaves.append(root)
        return

    for child in root.children:
        traverse(child, leaves)


def findLeaves(root: DecisionNode):
    leaves = []
    traverse(root, leaves)
    return leaves


def testError(root: DecisionNode, testSet: list):
    missed = 0

    for record in testSet:
        if predict(root, record[:len(record) - 1]) != record[-1]:
            missed += 1

    return float(missed) / float(len(testSet))


def checkPath(leaf: DecisionNode, testSet: list):
    # for every element in path
    node = leaf.parent

    while node is not None:

        substitute = DecisionNode.createLeaf(1, node.decisionValue, node.parent)

        error0 = testError(node, testSet)
        error1 = testError(substitute, testSet)

        if error0 > error1:
            node = DecisionNode.createLeaf(1, node.decisionValue, node.parent)

        node = node.parent


def C45(attributes: list, dataset: list, testSet):
    root = ID3(attributes, dataset, None, None)

    leaves = findLeaves(root)

    for leaf in leaves:
        checkPath(leaf, testSet)

    return root
