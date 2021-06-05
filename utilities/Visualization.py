from treelib import Tree
from trees.ID3 import *


def traverse(root: DecisionNode, visualTree: Tree, parentId: int):
    if root is None or root.isLeaf:
        return

    nextid = parentId

    for child in root.children:
        nextid += 1
        if child is None:
            visualTree.create_node("none", nextid, parent=parentId)
        else:
            if child.isLeaf:
                visualTree.create_node("l" + str(child.classValue), nextid, parent=parentId)
            else:
                visualTree.create_node("d" + str(child.attributeNumber), nextid,
                                       parent=parentId)
                nextid = traverse(child, visualTree, nextid)

    return nextid


def visualize(root: DecisionNode):
    tree = Tree()
    id = 0

    # l for leaves, d for decision nodes

    if root.isLeaf:
        tree.create_node("l" + str(root.classValue), id)
    else:
        tree.create_node("d" + str(root.attributeNumber), id)

    traverse(root, tree, id)

    tree.show()


def test():
    dataset2 = [[1, 1, 2, 0, 0], [2, 1, 4, 1, 1], [2, 2, 2, 2, 1], [2, 2, 0, 3, 1], [2, 3, 1, 4, 1],
                [1, 4, 0, 2, 1], [1, 1, 4, 3, 0], [1, 1, 1, 4, 1], [3, 1, 0, 1, 1], [4, 3, 0, 0, 0],
                [3, 2, 1, 4, 0], [4, 0, 2, 3, 1], [3, 4, 3, 2, 0], [4, 0, 4, 1, 0], [1, 2, 4, 0, 1]]

    attributes2 = [0, 1, 2, 3]

    print(attributes2[:2])
    print(attributes2[2:])

    dataset3 = [[0, 1, 0], [1, 1, 1], [1, 2, 1], [1, 2, 0], [1, 3, 1]]
    attributes3 = [0, 1]

    root = ID3(attributes3, dataset3, None, None)

    # root = ID3(attributes2, dataset2, None, None)

    #visualize(root)

test()