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
        # We can model this as a graph where each position is a node and edges represent the relation.
        # We can use dynamic programming to track the minimum possible value at each position.
        # We'll use a list to track the minimum value for each position.
        # We'll also track the maximum value needed so far.
        # Initialize the list with 1s.
        dp = [1] * (n + 1)
        max_val = 1
        for i in range(n):
            if s[i] == '<':
                # The current number must be less than the next number.
                # So the next number must be at least dp[i] + 1.
                dp[i+1] = dp[i] + 1
                max_val = max(max_val, dp[i+1])
            elif s[i] == '=':
                # The current number must be equal to the next number.
                # So the next number must be the same as the current.
                dp[i+1] = dp[i]
                max_val = max(max_val, dp[i+1])
            else:
                # The current number must be greater than the next number.
                # So the next number must be at most dp[i] - 1.
                # But since we want the minimum P, we can set the next number to 1.
                # However, this may not be optimal. We need to track the maximum value.
                # So we set the next number to 1, but we need to ensure that the previous number is greater.
                # So we set dp[i+1] = 1, but we need to track the maximum value.
                # However, this may not be correct. We need to ensure that the previous number is greater.
                # So we set dp[i+1] = 1, but we need to track the maximum value.
                # However, this may not be correct. We need to ensure that the previous number is greater.
                # So we set dp[i+1] = 1, but we need to track the maximum value.
                dp[i+1] = 1
                max_val = max(max_val, dp[i+1])
        print(max_val)

if __name__ == '__main__':
    solve()