class DecisionNode:
    def __init__(self, attributeNumber, decisionValue, parent):
        self.parent: [DecisionNode] = parent

        self.children: [DecisionNode] = [None] * 5

        # if not leaf node, then should stay None
        self.value = None

        # tells which child of parent node is this node
        self.decisionValue = decisionValue

        # decision this node makes
        self.attributeNumber = attributeNumber
