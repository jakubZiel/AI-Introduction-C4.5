//
// Created by jakub on 23.05.2021.
//

#include "DecisionNode.h"

DecisionNode::DecisionNode(int decisionNumber, int decisionValue, DecisionNode *parent): decisionNumber(decisionNumber), decisionValue(decisionValue){

    for (int i = 0; i < 5; i++)
        children[0] = nullptr;

    this->parent = parent;
}