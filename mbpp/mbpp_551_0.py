def check(candidate):
    assert candidate([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[1, 2, 1]
    assert candidate([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[3, -5, 1]
    assert candidate([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[1, 5, 1, 13, 5, 9]


def extract_column(data, column_index):
    return [row[column_index] for row in data]

check(extract_column)