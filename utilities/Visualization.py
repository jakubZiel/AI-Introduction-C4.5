from treelib import Tree

from trees.C45 import findLeaves, checkPath
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


def visualizeC45():
    dataset = ImportData.convert()
    attributes = list(range(54))

    teachingSetSize = int(len(dataset) * 0.90)

    root = ID3(attributes, dataset[:teachingSetSize], None, None)

    visualize(root)

    leaves = findLeaves(root)
    for leaf in leaves:
        if leaf is not None:
            checkPath(root, leaf, dataset[teachingSetSize:], leaves)

    visualize(root)
    return root
