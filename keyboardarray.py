from typing import List


def flatten(array: List[List[List[int]]]):
    rtrn = []
    for row in array:
        for column in row:
            rtrn.append(column)
    return rtrn


class KeyboardArray:
    kbarray = None

    def __init__(self) -> None:
        for i in range(21 * 6 * 3):
            self.kbarray[i] = 0
