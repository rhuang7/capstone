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
        max_sum = -float('inf')
        current_sum = 0
        start = 0
        end = 0
        for i in range(N):
            current_sum += A[i]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i + 1
            if current_sum < 0:
                current_sum = 0
        # Find the minimum length subarray with max sum
        # Since we already have the max_sum, we need to find the smallest subarray that gives this sum
        # Reset current_sum and find the subarray
        current_sum = 0
        min_len = N
        for i in range(N):
            current_sum += A[i]
            if current_sum == max_sum:
                min_len = min(min_len, i - start + 1)
            elif current_sum > max_sum:
                current_sum = 0
                start = i + 1
        results.append(str(min_len))
    print('\n'.join(results))