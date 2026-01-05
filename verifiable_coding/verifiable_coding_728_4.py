import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    matrix = []
    for _ in range(n):
        row = list(map(int, input[idx:idx+n]))
        matrix.append(row)
        idx += n
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][n-1-i]
    print(abs(primary_sum - secondary_sum))

if __name__ == '__main__':
    solve()