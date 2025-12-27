def check(candidate):
    assert candidate([[ 2 ], [3, 9 ], [1, 6, 7 ]]) == 6
    assert candidate([[ 2 ], [3, 7 ], [8, 5, 6 ]]) == 10 
    assert candidate([[ 3 ], [6, 4 ], [5, 2, 7 ]]) == 9


def minimum_total_path_sum(triangle):
    if not triangle:
        return 0
    
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update current cell with the minimum of the two possible paths
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The minimum path sum is at the top of the triangle
    return triangle[0][0]

check(minimum_total_path_sum)