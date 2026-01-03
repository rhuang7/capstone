import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        J = input[idx]
        S = input[idx+1]
        idx += 2
        count = 0
        for c in S:
            if c in J:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()