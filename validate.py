from utilities.Validation import *


def aggregateResults():
    print("No cross validation, entire dataset:")

    print("With cross validation:")
    for i in range(10, 4, -1):
        print("K = ", i)
        testMore(i, ID3, 10)
        testMore(i, C45, 10)


aggregateResults()

