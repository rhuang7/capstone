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
        max_len = 0
        # If K is 1, then the entire array is invalid (since there is only one flavor and it occurs in the whole array)
        if K == 1:
            results.append(0)
            continue
        # We need to find the longest subarray that does not contain at least one flavor
        # So we can find the longest subarray that contains all K flavors, and subtract it from N
        # But since we need at least one flavor not present, the maximum valid subarray is N - the minimum length of subarray containing all K flavors
        # So we find the minimum length of subarray containing all K flavors
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        min_len = float('inf')
        unique = 0
        for right in range(N):
            if count[A[right]] == 0:
                unique += 1
            count[A[right]] += 1
            while unique == K:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    unique -= 1
                left += 1
        if min_len == float('inf'):
            # All elements are same, so the maximum valid subarray is N-1
            results.append(N-1)
        else:
            results.append(N - min_len)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()