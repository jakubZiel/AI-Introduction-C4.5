from utilities.Validation import *
from CommercialTree import *


def aggregateResults():

    print ("Our own implementation.")
    print("Cross validation. K = 10")
    K = 10
    testNumber = 10     #number of tests to aggregate
    testMore(K, ID3, 10)
    testMore(K, C45, 10)

    print("Commercial implementation.")
    avg_commercial_error(testNumber)


aggregateResults()

