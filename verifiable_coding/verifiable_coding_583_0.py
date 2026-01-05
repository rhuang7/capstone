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
        total = sum(A)
        # We can adjust the sum by subtracting i * k for each i
        # The total sum can be adjusted by any multiple of the sum of i's
        # So we need to check if total can be adjusted to 0
        # The sum of i's from 1 to N is N*(N+1)//2
        sum_i = N * (N + 1) // 2
        # Check if total can be adjusted to 0 by subtracting multiples of sum_i
        # Since we can perform any number of operations, we can adjust the sum by any multiple of sum_i
        # So the question is: can we find k such that total - k * sum_i == 0
        # Which is equivalent to: total % sum_i == 0
        if sum_i == 0:
            # Only possible if total is 0
            results.append("YES" if total == 0 else "NO")
        else:
            results.append("YES" if total % sum_i == 0 else "NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()