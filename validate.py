from utilities.Validation import *


def aggregateResults():
    print("No cross validation, entire dataset:")

    print("With cross validation:")
    for i in range(10, 4, -1):
        print("K = ", i)
        test(i, ID3)
        test(i, C45)


aggregateResults()

