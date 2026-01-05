import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        A.sort()
        # The minimum time is (N-1) * 1, because we can adjust all but one to match the largest
        # Since we can add or subtract any odd number, we can adjust any number to any other number
        # in 1 second per difference (since we can choose the odd number to make the difference)
        # But since we can adjust any number to any other number in 1 second, the minimum time is
        # (N-1) * 1 = N-1
        results.append(str(N-1))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()