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
        # If K is 1, then the entire array is invalid (since there is no flavor not present)
        if K == 1:
            results.append(N)
            continue
        # Sliding window to find the longest subarray that misses at least one flavor
        # We need to find the longest subarray that does not contain all K flavors
        # So we can use a sliding window approach where we track the count of each flavor
        # and when all K flavors are present, we try to shrink the window from the left
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        unique = 0
        for right in range(N):
            flavor = A[right]
            if count[flavor] == 0:
                unique += 1
            count[flavor] += 1
            # If all K flavors are present, try to shrink the window
            while unique == K:
                left_flavor = A[left]
                count[left_flavor] -= 1
                if count[left_flavor] == 0:
                    unique -= 1
                left += 1
            # The current window is valid (missing at least one flavor)
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        results.append(max_len)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()