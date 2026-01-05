import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        k = int(data[idx])
        idx += 1
        q = int(data[idx])
        idx += 1
        queries = list(map(int, data[idx:idx + q]))
        idx += q
        
        # Brute force
        brute_count = 0
        brute_calls = 0
        def brute_force(key, from_idx):
            nonlocal brute_count, brute_calls
            brute_calls += 1
            if from_idx >= n:
                return 0
            if arr[from_idx] == key:
                brute_count += 1
                return 1 + brute_force(key, from_idx + 1)
            else:
                return brute_force(key, from_idx + 1)
        
        # DP
        dp = [None] * (n + 1)
        dp_calls = 0
        def dp_count(key, from_idx):
            nonlocal dp_calls
            if from_idx >= n:
                return 0
            if dp[from_idx] is not None:
                return dp[from_idx]
            dp_calls += 1
            if arr[from_idx] == key:
                dp[from_idx] = 1 + dp_count(key, from_idx + 1)
            else:
                dp[from_idx] = dp_count(key, from_idx + 1)
            return dp[from_idx]
        
        for a in queries:
            brute_count = 0
            brute_calls = 0
            brute_force(k, a)
            dp_count(k, a)
            results.append(f"{brute_count} {brute_calls} {dp_calls}")
    
    print('\n'.join(results))