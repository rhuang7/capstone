def check(candidate):
    assert candidate([ [1, 4, 5], [2, 0, 0 ] ], 3) == 7
    assert candidate([ [ 1, 2, 3, 4, 5], [ 6, 7, 8, 9, 10] ], 5) == 24
    assert candidate([ [7, 9, 11, 15, 19], [21, 25, 28, 31, 32] ], 5) == 81


def max_non_adjacent_sum(grid):
    if len(grid) != 2:
        raise ValueError("Grid must be 2 x n")
    
    n = len(grid[0])
    if n == 0:
        return 0
    
    # Initialize previous values
    prev1 = grid[0][0]
    prev2 = grid[1][0]
    
    for i in range(1, n):
        current1 = max(prev1, prev2 + grid[0][i])
        current2 = max(prev2, prev1 + grid[1][i])
        prev1, prev2 = current1, current2
    
    return max(prev1, prev2)

check(max_non_adjacent_sum)