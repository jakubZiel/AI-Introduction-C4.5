from utilities.Validation import *
from utilities.Visualization import *


def aggregateResults():
    print("No cross validation, entire dataset:")

    print("With cross validation:")
    for i in range(5, 1, -1):
        print("K = ", i)
        test(i, ID3)
        test(i, C45)


visualizeC45()
