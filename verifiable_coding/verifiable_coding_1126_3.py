import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for n in cases:
        if n == 0:
            print(1)
        else:
            print(2 * n * (n + 1) // 2 - n + 1)

if __name__ == '__main__':
    solve()