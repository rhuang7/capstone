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
        # If K is 1, then no subsegment can satisfy the condition
        if K == 1:
            results.append(0)
            continue
        # The maximum possible length is N if all K flavors are present
        # So we need to find the longest subsegment that is missing at least one flavor
        # We can use a sliding window approach
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(N):
            count[A[right]] += 1
            # Check if all K flavors are present in the current window
            while len(count) == K:
                # If all K are present, we need to shrink the window
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    del count[A[left]]
                left += 1
            # The current window is valid (missing at least one flavor)
            max_len = max(max_len, right - left + 1)
        results.append(max_len)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()