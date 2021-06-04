from typing import List


class DecisionNode:
    def __init__(self, isLeaf, attributeNumber, decisionValue, parent, classValue):
        self.parent: DecisionNode = parent

        self.children: List[DecisionNode] = [None] * 5

        self.isLeaf: bool = isLeaf
        # if not leaf node, then should stay None
        self.classValue: int = classValue

        # tells which child of parent node is this node
        self.decisionValue: int = decisionValue

        # decision this node makes
        self.attributeNumber: int = attributeNumber

    @staticmethod
    def createLeaf(classValue, parentDecision, parent):
        leaf = DecisionNode(True, None, parentDecision, parent, classValue)

        return leaf

    @staticmethod
    def createDecision(attributeNumber, parentDecision, parent):
        decision = DecisionNode(False, attributeNumber, parentDecision, parent, None)

        return decision
