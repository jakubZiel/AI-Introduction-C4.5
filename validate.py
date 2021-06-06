from utilities.Validation import *
from utilities.Visualization import *


def aggregateResults():
    print("No cross validation. Comparing look of trees for ID3 and C4.5:")
    visualizeC45()

    numberOfTests = 10

    print("With cross validation. Number of tests: ", numberOfTests)
    for i in range(5, 11):
        print("K = ", i)
        testMore(i, ID3, numberOfTests)
        testMore(i, C45, numberOfTests)

aggregateResults()
