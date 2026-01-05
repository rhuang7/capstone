import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx += 2
        if A > B:
            print('>')
        elif A < B:
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    solve()