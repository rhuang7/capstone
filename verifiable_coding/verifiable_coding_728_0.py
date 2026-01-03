import sys

def solve():
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    matrix = []
    index = 1
    for _ in range(n):
        row = list(map(int, input[index:index+n]))
        matrix.append(row)
        index += n
    
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][n-1-i]
    
    print(abs(primary_sum - secondary_sum))

if __name__ == '__main__':
    solve()