from DecisionNode import DecisionNode

root = DecisionNode(1, None, None)

root.children[0] = DecisionNode(2, 0, root)
root.children[1] = DecisionNode(2, 1, root)
root.children[2] = DecisionNode(2, 2, root)
root.children[3] = DecisionNode(2, 3, root)
root.children[4] = DecisionNode(2, 4, root)
