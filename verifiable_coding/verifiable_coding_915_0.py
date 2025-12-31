import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        n = int(input[idx])
        idx += 1
        days = list(map(int, input[idx:idx+n]))
        idx += n
        unique_days = set(days)
        results.append(str(len(unique_days)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()