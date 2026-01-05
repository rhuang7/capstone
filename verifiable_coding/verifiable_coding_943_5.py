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
        
        # dp[i][j] = number of ways to arrange i A's and j B's
        # with the constraint that if a plate has A, the previous plate cannot have B
        dp = [[0]*(W+1) for _ in range(V+1)]
        
        # Base case: 0 A's and 0 B's
        dp[0][0] = 1
        
        for i in range(V+1):
            for j in range(W+1):
                # If we place an A at the end, the previous plate cannot have B
                # So we can only add A to a state where the previous plate was A or nothing
                # So we can add A to dp[i-1][j] if i > 0
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # If we place a B at the end, the previous plate can have A or nothing
                # So we can add B to dp[i][j-1] if j > 0
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        print(dp[V][W])

if __name__ == '__main__':
    solve()