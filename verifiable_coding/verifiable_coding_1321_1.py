import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N == 1:
            print(0)
        else:
            print((N * (N - 1)) // 2 + (N - 1) * N // 2)

if __name__ == '__main__':
    solve()