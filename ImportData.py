import math
import numpy as np

def import_data():
    data = np.loadtxt('divorce.csv', delimiter=";", skiprows=1)
    data = data.astype(int)

    #test print
    print(data[0:5,:]) # first 5 rows