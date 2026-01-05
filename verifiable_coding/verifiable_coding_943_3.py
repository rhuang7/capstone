import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        V = int(data[index])
        W = int(data[index+1])
        index += 2
        
        # dp[i][j] represents the number of ways to arrange i A's and j B's
        # with the condition that if a plate has A, the previous plate cannot have B
        dp = [[0]*(W+1) for _ in range(V+1)]
        
        # Base case: 0 A's and 0 B's
        dp[0][0] = 1
        
        for i in range(V+1):
            for j in range(W+1):
                # If we place an A at the current position, the previous position cannot have B
                # So we can only add A if the previous position did not have B
                # This is handled by considering the previous state without B
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # If we place a B at the current position, the previous position can have A or B
                # But we need to ensure that if the previous position had B, then the current position can't have B
                # So we can only add B if the previous position did not have B
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        print(dp[V][W])

if __name__ == '__main__':
    solve()