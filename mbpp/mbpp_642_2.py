def check(candidate):
    assert candidate([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]] ) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}
    assert candidate([[(5, 6), (4, 3)], [(3, 3), (5, 7)], [(4, 3), (5, 6)]] ) == {((4, 3), (5, 6)), ((3, 3), (5, 7))}
    assert candidate([[(6, 7), (5, 4)], [(4, 4), (6, 8)], [(5, 4), (6, 7)]] ) =={((4, 4), (6, 8)), ((5, 4), (6, 7))}


def remove_similar_rows(matrix):
    if not matrix:
        return []
    
    unique_rows = []
    for row in matrix:
        if row not in unique_rows:
            unique_rows.append(row)
    return unique_rows

check(remove_similar_rows)