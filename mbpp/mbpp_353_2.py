def check(candidate):
    assert candidate([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[[2, 3], [4, 5], [1, 1]]
    assert candidate([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[[1, 2], [-2, 4], [1, -1]]
    assert candidate([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[[3], [7], [3], [15, 17], [7], [11]]


def remove_column(data, column_index):
    if not data:
        return []
    return [row[:column_index] + row[column_index+1:] for row in data]

check(remove_column)