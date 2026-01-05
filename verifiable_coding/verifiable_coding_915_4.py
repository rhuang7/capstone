import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        idx += 1
        days = list(map(int, input[idx:idx+n]))
        idx += n
        unique_days = set(days)
        print(len(unique_days))

if __name__ == '__main__':
    solve()