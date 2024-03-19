import math


def correlation_coefficient(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('The length of the two lists must be the same!')

    xy = 0
    for i in range(len(list_1)):
        xy += (list_1[i] * list_2[i])

    x_sum = sum(list_1)
    y_sum = sum(list_2)

    x_squared_elements = (sum([el ** 2 for el in list_1]))
    y_squared_elements = (sum([el ** 2 for el in list_2]))
    return ((len(list_1) * xy) - (x_sum * y_sum)) \
           / math.sqrt((
            (len(list_1) * x_squared_elements - x_sum ** 2) *
            (len(list_1) * y_squared_elements - y_sum ** 2)))


math_test = [11, 13, 18, 12, 16, 14]
intelligence_test = [67, 73, 78, 71, 73, 70]

print(correlation_coefficient(math_test, intelligence_test))
