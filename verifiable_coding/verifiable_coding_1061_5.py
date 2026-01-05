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
        ops = [''] + ops
        n = len(ops)
        # dp[i][j] = maximum value of expression from i-th to j-th operand
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = -1
                for k in range(i + 1, j):
                    val = -1
                    if ops[k] == '&':
                        val = nums[i] & nums[j]
                    elif ops[k] == '|':
                        val = nums[i] | nums[j]
                    elif ops[k] == '^':
                        val = nums[i] ^ nums[j]
                    if val > dp[i][j]:
                        dp[i][j] = val
                    if dp[i][k-1] != -1 and dp[k][j] != -1:
                        val = dp[i][k-1] & dp[k][j]
                        if val > dp[i][j]:
                            dp[i][j] = val
                        val = dp[i][k-1] | dp[k][j]
                        if val > dp[i][j]:
                            dp[i][j] = val
                        val = dp[i][k-1] ^ dp[k][j]
                        if val > dp[i][j]:
                            dp[i][j] = val
        return dp[0][n-1]
    
    for case in cases:
        print(max_expression(case))
        
if __name__ == '__main__':
    solve()