def check(candidate):
    assert candidate([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2) == 14
    assert candidate([[13, 0, 0], [7, 4, 0], [2, 4, 6]], 2, 2) == 24 
    assert candidate([[2, 0, 0], [11, 18, 0], [21, 25, 33]], 2, 2) == 53


def max_path_sum(triangle):
    if not triangle:
        return 0
    
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update current cell with the maximum of the two paths below it
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    # The top cell now contains the maximum path sum
    return triangle[0][0]

check(max_path_sum)