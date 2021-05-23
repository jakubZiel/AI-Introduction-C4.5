//
// Created by jakub on 23.05.2021.
//

#ifndef C4_5_DIVORCES_DECISIONNODE_H
#define C4_5_DIVORCES_DECISIONNODE_H


class DecisionNode {
public:
    DecisionNode* children[5]{};

    int decisionNumber;

    //tells which child of parent node this node is
    int decisionValue;

    DecisionNode* parent;

    //not null only in leaf node
    bool* divorced{};


    DecisionNode(int decisionNumber, int decisionValue, DecisionNode* parent);
};


#endif //C4_5_DIVORCES_DECISIONNODE_H
