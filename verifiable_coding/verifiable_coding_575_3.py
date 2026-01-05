import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        if n == 0:
            print(1)
            continue
        
        # We need to find the minimum P such that we can assign numbers to the N+1 positions
        # such that the relations between consecutive numbers are satisfied.
        # We can model this as a graph where each position is a node and edges represent the required relation.
        # We need to find the longest path in this graph, as the minimum P will be the length of the longest path.
        
        # We can use dynamic programming to track the minimum value at each position.
        # We'll track the minimum and maximum values at each position.
        # For each position i, we'll track the minimum value that can be placed there such that the relations are satisfied.
        
        # Initialize the dp array with 0s
        dp = [0] * (n + 1)
        
        # For the first position, we can assign 1
        dp[0] = 1
        
        for i in range(n):
            # The current sign is s[i]
            if s[i] == '<':
                # The next number must be greater than the current one
                dp[i+1] = dp[i] + 1
            elif s[i] == '>':
                # The next number must be less than the current one
                dp[i+1] = 1
            else:
                # The next number must be equal to the current one
                dp[i+1] = dp[i]
        
        print(dp[-1])
        
if __name__ == '__main__':
    solve()