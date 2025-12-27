def check(candidate):
    assert candidate(2) == 2
    assert candidate(3) == 5
    assert candidate(4) == 15


def bell_number(n):
    # Initialize a 2D list to store Bell numbers
    bell = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: Bell number for 0 is 1
    bell[0][0] = 1
    
    # Fill the Bell triangle
    for i in range(1, n + 1):
        # First column is the sum of the previous row
        bell[i][0] = sum(bell[i-1])
        for j in range(1, i + 1):
            bell[i][j] = bell[i-1][j-1] + bell[i-1][j]
    
    return bell[n][0]

check(bell_number)