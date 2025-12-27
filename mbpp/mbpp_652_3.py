def check(candidate):
    assert candidate([[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]) == '[(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]'
    assert candidate([[(5, 6), (8, 9)], [(11, 14), (19, 18)], [(1, 5), (11, 2)]]) == '[(5, 8, 11, 19, 1, 11), (6, 9, 14, 18, 5, 2)]'
    assert candidate([[(6, 7), (9, 10)], [(12, 15), (20, 21)], [(23, 7), (15, 8)]]) == '[(6, 9, 12, 20, 23, 15), (7, 10, 15, 21, 7, 8)]'


def flatten_tuple_matrix(matrix):
    if not matrix:
        return ()
    
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Create a result tuple list
    result = ()
    
    # Iterate over each column index
    for col in range(cols):
        # Create a tuple for the current column
        column_tuple = tuple(matrix[row][col] for row in range(rows))
        result += (column_tuple,)
    
    return result

check(flatten_tuple_matrix)