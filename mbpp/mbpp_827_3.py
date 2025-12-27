def check(candidate):
    assert candidate( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],0)==12
    assert candidate( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],1)==15
    assert candidate( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],3)==9


def sum_column(data, column_index):
    if not data or column_index < 0:
        return 0
    return sum(row[column_index] for row in data)

check(sum_column)