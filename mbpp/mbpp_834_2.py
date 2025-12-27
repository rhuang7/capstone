def check(candidate):
    assert candidate(3)==[[1, 2, 3], [8, 9, 4], [7, 6, 5]] 
    assert candidate(2)==[[1,2],[4,3]]
    assert candidate(7)==[[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49, 44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]]


def generate_spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n-1, 0, n-1

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

check(generate_spiral_matrix)