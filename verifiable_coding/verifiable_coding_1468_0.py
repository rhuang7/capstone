import sys

def solve():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    cases = data[1:T+1]
    for case in cases:
        print(int(case, 16))

if __name__ == '__main__':
    solve()