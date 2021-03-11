"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    a = 0
    for i in array:
        if array[a] == 0 and not isinstance(array[a], bool):
            del array[a]
            array.append(0)
        else:
            a += 1         
    return array 