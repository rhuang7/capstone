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
        
        # We need to determine if Vanja can force the absolute value of the expression to be >= K
        # We use dynamic programming to track possible values of the expression
        # dp[i][v] = True if it is possible to reach value v after i operations
        # Since the maximum possible value is 1*sum(A) and minimum is -sum(A), we can use a set to track possible values
        
        sum_A = sum(A)
        max_val = sum_A
        min_val = -sum_A
        
        # Initialize dp
        dp = [set() for _ in range(N+1)]
        dp[0].add(0)
        
        for i in range(N):
            for val in dp[i]:
                # Current player can choose + or -
                dp[i+1].add(val + A[i])
                dp[i+1].add(val - A[i])
        
        # Check if any value in dp[N] has absolute value >= K
        vanja_wins = any(abs(v) >= K for v in dp[N])
        results.append(1 if vanja_wins else 2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()