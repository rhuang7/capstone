import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        # Group consecutive characters
        groups = []
        prev = s[0]
        count = 1
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                groups.append((prev, count))
                prev = c
                count = 1
        groups.append((prev, count))
        
        # Calculate the total number of 1s
        total_ones = sum(count for char, count in groups if char == '1')
        
        # If there are no 1s, Alice's score is 0
        if total_ones == 0:
            print(0)
            continue
        
        # Use dynamic programming to find the optimal play
        n = len(groups)
        dp = [[0] * 2 for _ in range(n)]
        
        # Fill dp for even and odd turns
        for i in range(n):
            if i % 2 == 0:
                # Alice's turn
                dp[i][0] = max(dp[i-1][1] + groups[i][1] if groups[i][0] == '1' else 0, dp[i-1][0])
            else:
                # Bob's turn
                dp[i][1] = max(dp[i-1][0] + groups[i][1] if groups[i][0] == '1' else 0, dp[i-1][1])
        
        print(dp[n-1][0] if n % 2 == 0 else dp[n-1][1])

if __name__ == '__main__':
    solve()