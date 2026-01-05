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
        s = data[idx]
        idx += 1
        if k % 2 != 0:
            results.append("NO")
            continue
        if k > n:
            results.append("NO")
            continue
        # For the string to be k-balanced, every substring of length k must have exactly k/2 0s and 1s
        # So for any i, the number of 0s in s[i:i+k] must equal the number of 1s
        # This implies that for any i, the number of 0s in s[i:i+k] must be exactly k//2
        # We can model this as a system of equations
        # Let's consider the difference between the number of 0s and 1s in the string
        # For the string to be k-balanced, the difference between 0s and 1s in any k-length substring must be 0
        # This can be modeled using a difference array
        diff = [0] * (n + 1)
        for i in range(n):
            if s[i] == '0':
                diff[i+1] += 1
            elif s[i] == '1':
                diff[i+1] -= 1
        # Now, for the string to be k-balanced, the difference between diff[i+k] and diff[i] must be 0
        # So for all i in 0 <= i <= n - k, diff[i+k] - diff[i] must be 0
        # This gives us a system of constraints
        # We can check for each position i, the number of 0s and 1s in the substring s[i:i+k] must be equal
        # We can do this by checking the difference array
        possible = True
        for i in range(n - k + 1):
            if diff[i+k] - diff[i] != 0:
                possible = False
                break
        if not possible:
            results.append("NO")
            continue
        # Now, we need to check if the string can be filled with 0s and 1s such that the constraints are satisfied
        # We can do this by checking the difference array and ensuring that the constraints are compatible
        # We can use a greedy approach to fill in the string
        # We can start from the first character and fill in the rest based on the constraints
        # We can use a variable to track the current difference
        current_diff = 0
        res = []
        for i in range(n):
            if s[i] == '0':
                res.append('0')
                current_diff += 1
            elif s[i] == '1':
                res.append('1')
                current_diff -= 1
            else:
                # We can choose either 0 or 1, but we need to ensure that the difference remains consistent
                # We can choose based on the constraints
                # For the substring s[i:i+k], the difference must be 0
                # So, for the current position i, the difference between the current and the next k positions must be 0
                # We can check if the current_diff + (number of 0s in the next k positions) - (number of 1s in the next k positions) is 0
                # But this is complicated, so we can use a different approach
                # We can look at the next k positions and see what the difference should be
                # We can use the difference array to determine what the current character should be
                # For the substring s[i:i+k], the difference must be 0
                # So, the difference between diff[i+k] and diff[i] must be 0
                # This is already checked earlier, so we can proceed
                # We can choose the character based on the current_diff and the constraints
                # For example, if the current_diff is positive, we can choose 1 to decrease it
                # If it's negative, we can choose 0 to increase it
                # If it's zero, we can choose either
                if current_diff > 0:
                    res.append('1')
                    current_diff -= 1
                elif current_diff < 0:
                    res.append('0')
                    current_diff += 1
                else:
                    res.append('0')
                    current_diff += 1
        # Now, we need to check if the final string is k-balanced
        # We can check the difference array again
        diff = [0] * (n + 1)
        for i in range(n):
            if res[i] == '0':
                diff[i+1] += 1
            elif res[i] == '1':
                diff[i+1] -= 1
        possible = True
        for i in range(n - k + 1):
            if diff[i+k] - diff[i] != 0:
                possible = False
                break
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))