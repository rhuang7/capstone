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
        
        # dp[i][j] represents the number of ways to arrange i dishes of A and j dishes of B
        dp = [[0] * (W + 1) for _ in range(V + 1)]
        
        # Base case: 0 dishes of A and 0 dishes of B
        dp[0][0] = 1
        
        for i in range(V + 1):
            for j in range(W + 1):
                # If we place a dish of A at the end, we can do it if the previous dish was not B
                # So we can take dp[i-1][j] (previous dish was A) or dp[i-1][j-1] (previous dish was B)
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # If we place a dish of B at the end, we can do it if the previous dish was not A
                # So we can take dp[i][j-1] (previous dish was B) or dp[i-1][j-1] (previous dish was A)
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        print(dp[V][W])

if __name__ == '__main__':
    solve()