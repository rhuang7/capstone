import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        expr = input[idx].decode()
        idx += 1
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
        ops = ['&', '(', ')']  # Placeholder, will be replaced
        # We need to evaluate all possible parenthesizations
        # But since the number of operators is small (<=10), we can use dynamic programming
        # Let's use a DP approach where dp[i][j] is the maximum value of the subexpression from i to j
        n = len(nums) - 1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 2):
                j = i + length - 1
                dp[i][j] = -1
                for k in range(i + 1, j):
                    for op in ['&', '|', '^']:
                        if ops[k - 1] == op:
                            val = 0
                            if op == '&':
                                val = nums[i] & dp[k][j]
                            elif op == '|':
                                val = nums[i] | dp[k][j]
                            elif op == '^':
                                val = nums[i] ^ dp[k][j]
                            if dp[i][j] == -1 or val > dp[i][j]:
                                dp[i][j] = val
        print(dp[0][n])

if __name__ == '__main__':
    solve()