import numpy as np


def import_data(filePath):
    data = np.loadtxt(filePath, delimiter=";", skiprows=1)
    data = data.astype(int)


    # test print
    print(data[0:5, :])  # first 5 rows

    return data