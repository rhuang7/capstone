import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T+1):
        N = input[i]
        reversed_N = int(str(N)[::-1])
        print(reversed_N)

if __name__ == '__main__':
    solve()