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
        
        # We need to determine if Vanja can force |V| >= K
        # Since players alternate and start with Vanja, we simulate the game
        # We use dynamic programming to track the possible values of the expression
        # at each step
        
        # dp[i][v] = True if it's possible to reach value v after i operations
        # We use a set to track possible values at each step
        dp = [set() for _ in range(N+1)]
        dp[0].add(0)
        
        for i in range(N):
            for v in dp[i]:
                # Current player can choose + or -
                # The next value is v + A[i] or v - A[i]
                dp[i+1].add(v + A[i])
                dp[i+1].add(v - A[i])
        
        # After all operations, check if any value has absolute value >= K
        max_abs = 0
        for v in dp[N]:
            max_abs = max(max_abs, abs(v))
        
        if max_abs >= K:
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()