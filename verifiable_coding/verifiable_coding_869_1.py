import sys

def solve():
    M = sys.stdin.buffer.readline().decode().strip()
    S = sys.stdin.buffer.readline().decode().strip()
    if S in M:
        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    solve()