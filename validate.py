from utilities.Validation import *


def aggregateResults():
    print("No cross validation, entire dataset:")

    print("With cross validation:")
    for i in range(10, 5, -1):
        print("K = ", i)
        testMore(i, ID3, 5)
        testMore(i, C45, 5)


aggregateResults()

