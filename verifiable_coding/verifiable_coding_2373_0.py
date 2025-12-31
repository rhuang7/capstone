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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # For each pair (i, n-i+1), we need to find a value x such that a[i] + a[n-i+1] = x
        # We need to find the x that requires the least number of replacements
        # We can try all possible x values between 2 and 2k (since each a[i] is at least 1 and at most k)
        # But since k can be up to 2e5, we need an efficient way to find the optimal x
        
        # First, we collect all possible x values that can be formed from the current pairs
        # and then for each possible x, compute the number of replacements needed
        
        # We can use a frequency dictionary to count how many pairs can form a given x
        # Then, for each x, compute the number of replacements needed
        # The x with the minimum replacements is our answer
        
        # To optimize, we can try all possible x values between 2 and 2k
        # But since k can be up to 2e5, we need to limit the x values to those that are possible
        # We can collect all possible x values from the current pairs and try those
        
        # Collect all possible x values from the current pairs
        possible_x = set()
        for i in range(n // 2):
            x = a[i] + a[n - i - 1]
            possible_x.add(x)
        
        # Also consider x values that can be formed by replacing one of the elements
        # For example, if a[i] is 1 and a[n-i-1] is k, then x can be 2 to 2k
        # So we need to consider all x values between 2 and 2k
        # But since k can be up to 2e5, we need to limit this to a reasonable range
        
        # We will try all x values between 2 and 2k
        min_replacements = float('inf')
        for x in range(2, 2 * k + 1):
            replacements = 0
            for i in range(n // 2):
                a_i = a[i]
                a_j = a[n - i - 1]
                # Check if a_i + a_j == x
                # If not, we need to replace one of them
                # We can replace the one that requires the least changes
                # For example, if a_i + a_j < x, we can replace a_j to x - a_i
                # Or replace a_i to x - a_j
                # We need to choose the one that requires the least changes
                # But since we are trying to minimize the total replacements, we can just count how many pairs need to be changed
                # For each pair, if a_i + a_j != x, we need to replace at least one of them
                # So for each pair, if a_i + a_j != x, we need to count 1 replacement
                # But we can do better by checking if one of the elements can be adjusted to make the sum x
                # For example, if a_i + a_j < x, we can replace a_j to x - a_i
                # But x - a_i must be between 1 and k
                # Similarly for a_i
                # So for each pair, we can check if it's possible to adjust one of the elements to make the sum x
                # If not, we need to replace both
                # But since we are trying to find the x that requires the least replacements, we can just count the number of pairs that need to be changed
                # For this problem, we can just count the number of pairs that need to be changed
                # Because for each such pair, we need to replace at least one element
                # So the total number of replacements is the number of such pairs
                # So we can just count the number of pairs that do not satisfy a_i + a_j == x
                # But we can also check if it's possible to adjust one element to make the sum x
                # If so, we don't need to replace both
                # So for each pair, we check if it can be adjusted to x with at most one replacement
                # If not, we need to replace both
                # So for each pair, we can check if a_i + a_j is in [x - k, x] or [x, x + k]
                # Wait, no. We need to find if one of the elements can be adjusted to make the sum x
                # For example, if a_i + a_j < x, then we can replace a_j to x - a_i
                # But x - a_i must be in [1, k]
                # So if x - a_i is in [1, k], then we can replace a_j
                # Similarly, if a_i > x - 1, then we can replace a_i
                # So for each pair, we can check if it can be adjusted to x with one replacement
                # If not, we need to replace both
                # So for each pair, we can check if it can be adjusted to x with one replacement
                # If not, we need to replace both
                # So the total number of replacements is the number of pairs that cannot be adjusted to x with one replacement
                # So for each pair, we check if a_i + a_j is in [x - k, x + k]
                # But that's not correct. Let's think again.
                # For a pair (a_i, a_j), we need to make a_i + a_j = x
                # So we can replace a_i to x - a_j, but x - a_j must be in [1, k]
                # Or replace a_j to x - a_i, but x - a_i must be in [1, k]
                # So for the pair (a_i, a_j), we can check if either of these is possible
                # If yes, then we can replace one of them
                # If not, then we need to replace both
                # So for each pair, we can check if either of the two options is possible
                # If not, we need to replace both
                # So for each pair, we can check if it can be adjusted with one replacement
                # If not, we need to replace both
                # So for each pair, the number of replacements needed is 0 if it can be adjusted with one replacement, else 2
                # But we can optimize this by checking if a_i + a_j is in [x - k, x + k]
                # Wait, no. Let's think again.
                # We can replace a_i to x - a_j, but x - a_j must be in [1, k]
                # So 1 <= x - a_j <= k
                # => x - k <= a_j <= x - 1
                # Similarly, if we replace a_j to x - a_i, then 1 <= x - a_i <= k
                # => x - k <= a_i <= x - 1
                # So for a pair (a_i, a_j), we can check if a_j is in [x - k, x - 1] or a_i is in [x - k, x - 1]
                # If either is true, then we can replace one of them
                # If not, then we need to replace both
                # So for each pair, the number of replacements needed is:
                # 0 if a_i + a_j == x
                # 1 if either a_i or a_j can be adjusted to make the sum x
                # 2 otherwise
                # But we can check this more efficiently
                # For the current x, we can check if a_i + a_j == x
                # If not, we can check if a_i + a_j is in [x - k, x + k]
                # Wait, no. Let's think again.
                # For a pair (a_i, a_j), the possible values of a_i + a_j after replacement is x
                # So we need to find if there exists a value for a_i or a_j such that the sum is x
                # So for a_i, we can set it to x - a_j, but x - a_j must be in [1, k]
                # So 1 <= x - a_j <= k
                # => x - k <= a_j <= x - 1
                # Similarly, for a_j, we can set it to x - a_i, but x - a_i must be in [1, k]
                # => x - k <= a_i <= x - 1
                # So for a pair (a_i, a_j), if either a_i is in [x - k, x - 1] or a_j is in [