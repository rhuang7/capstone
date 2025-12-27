def check(candidate):
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],1)==[2,5,1]


def extract_elements(matrix, index=0):
    """
    Extracts every first or specified element from a given two-dimensional list.
    """
    return [row[index] for row in matrix]

check(extract_elements)