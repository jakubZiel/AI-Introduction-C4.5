from treelib import Tree, Node
from DecisionNode import DecisionNode
from ID3 import *


def traverse(root: DecisionNode, visualTree: Tree):
    if root is None or root.isLeaf:
        return

    for child in root.children:
        if child is None:
            visualTree.create_node("none", "none", "d" + str(root.attributeNumber))
        else:
            if child.isLeaf:
                visualTree.create_node(str(child.classValue), str(child.classValue), "d" + str(root.attributeNumber))
            else:
                visualTree.create_node("d" + str(child.attributeNumber), "d" + str(child.attributeNumber),
                                       "d" + str(root.attributeNumber))
                traverse(child, visualTree)


def visualize(root: DecisionNode):
    tree = Tree()

    if root.isLeaf:
        tree.create_node(str(root.classValue), str(root.classValue))
    else:
        tree.create_node("d" + str(root.attributeNumber), "d" + str(root.attributeNumber))

    traverse(root, tree)

    return tree


def test():
    dataset2 = [[1, 1, 2, 0, 0], [2, 1, 4, 1, 1], [2, 2, 2, 2, 1], [2, 2, 0, 3, 1], [2, 3, 1, 4, 1],
                [1, 4, 0, 2, 1], [1, 1, 4, 3, 0], [1, 1, 1, 4, 1], [3, 1, 0, 1, 1], [4, 3, 0, 0, 0],
                [3, 2, 1, 4, 0], [4, 0, 2, 3, 1], [3, 4, 3, 2, 0], [4, 0, 4, 1, 0], [1, 2, 4, 0, 1]]

    attributes2 = [0, 1, 2, 3]

    root = ID3(attributes2, dataset2, None, None)

    visualizedTree = visualize(root)
    visualizedTree.show()

test()