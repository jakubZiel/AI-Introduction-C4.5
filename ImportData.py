import random
import numpy as np


def import_data(filePath):
    data = np.loadtxt(filePath, delimiter=";", skiprows=1)
    data = data.astype(int)

    # test print
    print(data[0:5, :])  # first 5 rows

    return data


def convert():
    data = import_data("data/divorce.csv")

    output = []

    for record in data:
        n_record = []
        for i in record:
            n_record.append(i)

        # n_record[-1] = random.randint(0, 1)
        output.append(n_record)

    return output
