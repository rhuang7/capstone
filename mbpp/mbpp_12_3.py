def check(candidate):
    assert candidate([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert candidate([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert candidate([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]


def sort_matrix_by_row_sum(matrix):
    # Sort the matrix based on the sum of each row
    return sorted(matrix, key=lambda row: sum(row))

check(sort_matrix_by_row_sum)