import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    for i in range(1, n+1):
        t = int(input[i])
        result = 1
        for j in range(1, t+1):
            result *= j
        print(result)

if __name__ == '__main__':
    solve()