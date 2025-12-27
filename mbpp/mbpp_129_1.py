def check(candidate):
    assert candidate([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False


def is_magic_square(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False
    
    # Calculate the sum of the first row
    magic_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check columns
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != magic_sum:
            return False
    
    # Check diagonals
    diag1 = sum(matrix[i][i] for i in range(n))
    diag2 = sum(matrix[i][n-1-i] for i in range(n))
    if diag1 != magic_sum or diag2 != magic_sum:
        return False
    
    return True

def create_magic_square(n):
    if n == 1:
        return [[1]]
    
    # Initialize magic square
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    
    # Start position
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        # Calculate next position
        ni = (i - 1) % n
        nj = (j + 1) % n
        if magic_square[ni][nj] != 0:
            ni = (i + 1) % n
            nj = j
        i, j = ni, nj
    
    return magic_square

check(create_magic_square)