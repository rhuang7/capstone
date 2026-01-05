import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for K in cases:
        for i in range(K):
            row = ''.join(str((i + j) % 10) for j in range(K))
            print(row)
        for i in range(K-1, 0, -1):
            row = ''.join(str((i + j) % 10) for j in range(K))
            print(row)

if __name__ == '__main__':
    solve()