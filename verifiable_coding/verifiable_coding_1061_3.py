import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:]
    
    def max_expression(expr):
        ops = []
        nums = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                num = 0
                while i < len(expr) and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    i += 1
                nums.append(num)
            else:
                ops.append(expr[i])
                i += 1
        nums = [0] + nums
        ops = ['&', ']', '|', '^', '']  # Placeholder for the last operator
        # Try all possible orders of operations
        from itertools import permutations
        max_val = 0
        for perm in permutations(ops):
            # Evaluate the expression with the given operator order
            # This is a simplified approach for small number of operators
            # (since the number of operators is at most 10, but permutations would be too large)
            # Instead, we use a recursive approach to evaluate all possible groupings
            # This is a simplified version for the problem constraints
            # We use a dynamic programming approach to find the maximum value
            # We use a memoization approach to store the maximum value for sub-expressions
            # We use a DP table where dp[i][j] represents the maximum value of the sub-expression from i to j
            n = len(nums) - 1
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                dp[i][i] = nums[i]
            for length in range(2, n + 1):
                for i in range(n - length + 2):
                    j = i + length - 1
                    dp[i][j] = -1
                    for k in range(i + 1, j + 1):
                        if perm[k - i - 1] == '&':
                            val = nums[i] & nums[k]
                            if dp[i][k - 1] != -1 and dp[k][j] != -1:
                                dp[i][j] = max(dp[i][j], dp[i][k - 1] & dp[k][j])
                        elif perm[k - i - 1] == '|':
                            val = nums[i] | nums[k]
                            if dp[i][k - 1] != -1 and dp[k][j] != -1:
                                dp[i][j] = max(dp[i][j], dp[i][k - 1] | dp[k][j])
                        elif perm[k - i - 1] == '^':
                            val = nums[i] ^ nums[k]
                            if dp[i][k - 1] != -1 and dp[k][j] != -1:
                                dp[i][j] = max(dp[i][j], dp[i][k - 1] ^ dp[k][j])
            return dp[0][n]
        return max_val
    
    for expr in cases:
        print(max_expression(expr))

if __name__ == '__main__':
    solve()