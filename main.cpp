#include <iostream>

#include "DecisionTree/DecisionNode.h"

int main() {


    DecisionNode root(1, -1, nullptr);


    root.children[0] = new DecisionNode(2, 0 , &root);
    root.children[1] = new DecisionNode(2, 1 , &root);
    root.children[2] = new DecisionNode(2, 2 , &root);
    root.children[3] = new DecisionNode(2, 3 , &root);
    root.children[4] = new DecisionNode(2, 4 , &root);


    root.children[2]->children[0] = new DecisionNode(3, 0, root.children[2]);
    root.children[2]->children[1] = new DecisionNode(3, 1, root.children[2]);
    root.children[2]->children[2] = new DecisionNode(3, 2, root.children[2]);
    root.children[2]->children[3] = new DecisionNode(3, 3, root.children[2]);
    root.children[2]->children[4] = new DecisionNode(3, 4, root.children[2]);


}
