import math


def infSet(data_set):
    # type: ([]) ->  float

    divorce_false = 0
    divorce_true = 0

    data_size = len(data_set)

    for element in data_set:
        if not element:
            divorce_false += 1
        else:
            divorce_true += 1

    divorce_false /= data_size
    divorce_true /= data_size

    return - (divorce_false * math.log(divorce_false) + divorce_true * math.log(divorce_true))


def infGain(attribute, data_set):
    # type: (int, []) -> float

    return 0.0
