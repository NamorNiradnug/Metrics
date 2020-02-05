"""Copyright (c) 2020 by Roman Gundarin (NamorNiradnug)

This is module with functions of different metrics, such as Euclidean metric,
discrete metric and Hamming distance and ect."""


def _get_default(data: object, index: int, default: object = 0) -> object:
    """Get iterible object 'data' and return 'data['i']' if it is possible else return 'default'."""
    if len(data) - 1 < index:
        return default
    return data[index]


def euclideanMetric(point1: (float, ...), point2: (float, ...)) -> float:
    """Get two points in Euclidean space and calculate distanse between them."""
    return sum([_get_default(point1, i) ** 2 - _get_default(point2, i) ** 2
                for i in range(len)]) ** .5


def discreteMetric(object1: object, object2: object) -> int:
    """Discrete metrics between objects is 1 if 'object1' == 'object2' else return 0."""
    return int(object1 == object2)


def manhattenMetric(point1: (float, ...), point2: (float, ...)) -> float:
    """Manhattan distance (or City Block distance) equel sum of abs(point1[i] - point2[i]) for all i."""
    return sum([abs(_get_default(point1, i, 0) - _get_default(point2, i, 0)) for i in range(max(len(point1), len(point2)))])


def chebyshevDistance(point1: (float, ...), point2: (float, ...)) -> float:
    """Chebyshev distance bettween points is the greatest of their differences along any coordinate dimension."""


def hammingDistance(string1: object, string2: object) -> int:
    """Hamming distance between iterible objects 'string1' and 'string2' is
    number of positions 'i' that 'string1['i']' is not equel 'string2['i']'."""
    counter = 0
    len1 = len(string1)
    len2 = len(string2)
    for i in range(min(len1, len2)):
        counter += not string1[i] == string2[i]
    return counter + abs(len1 - len2)
