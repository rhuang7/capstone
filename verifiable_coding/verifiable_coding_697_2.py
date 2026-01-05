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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        max_sum = -float('inf')
        current_sum = sum(A[:K])
        max_sum = current_sum
        for i in range(1, N - K + 1):
            current_sum = current_sum - A[i-1] + A[i+K-1]
            if current_sum > max_sum:
                max_sum = current_sum
        results.append(str(max_sum))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()