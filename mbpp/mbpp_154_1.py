def check(candidate):
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert candidate([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],3)==[2,2,5]


def extract_elements(matrix, indices):
    return [row[i] for row in matrix for i in indices if i < len(row)]

check(extract_elements)