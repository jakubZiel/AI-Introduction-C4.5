#include <iostream>

#include "DecisionTree/DecisionNode.h"

int main() {


    DecisionNode root(1, -1, nullptr);


    root.children[0] = new DecisionNode(2, 0 , &root);
    root.children[1] = new DecisionNode(2, 1 , &root);
    root.children[2] = new DecisionNode(2, 2 , &root);
    root.children[3] = new DecisionNode(2, 3 , &root);
    root.children[4] = new DecisionNode(2, 4 , &root);



}
