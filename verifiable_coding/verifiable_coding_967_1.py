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
        M = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Use dynamic programming to count subsets that sum to M
        dp = [0] * (M + 1)
        dp[0] = 1  # Base case: one way to make sum 0 (select nothing)
        
        for num in A:
            for j in range(M, num - 1, -1):
                dp[j] += dp[j - num]
        
        results.append(dp[M])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()