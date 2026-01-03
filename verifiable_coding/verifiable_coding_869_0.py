import sys

def solve():
    M = sys.stdin.buffer.read().split()[0]
    S = sys.stdin.buffer.read().split()[0]
    if S in M:
        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    solve()