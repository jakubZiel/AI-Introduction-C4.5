import numpy as np


def import_data(filePath):
    data = np.loadtxt(filePath, delimiter=";", skiprows=1)
    data = data.astype(int)
    return data


def convert(file_path):
    data = import_data(file_path)

    output = []

    for record in data:
        n_record = []
        for i in record:
            n_record.append(i)

        output.append(n_record)

    return output
