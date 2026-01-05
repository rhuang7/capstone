import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:]
    
    def max_expr(expr):
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
        ops = ['&', ' ', '|', ' ', '^']
        # Try all possible operator orders
        from itertools import permutations
        max_val = 0
        for perm in permutations(ops):
            # Build the expression with the current permutation
            expr = []
            for i in range(len(perm)):
                expr.append(str(nums[i]))
                expr.append(perm[i])
            expr.append(str(nums[-1]))
            # Evaluate the expression
            val = nums[0]
            for i in range(len(perm)):
                op = perm[i]
                num = nums[i + 1]
                if op == '&':
                    val &= num
                elif op == '|':
                    val |= num
                elif op == '^':
                    val ^= num
            max_val = max(max_val, val)
        return max_val
    
    for case in cases:
        print(max_expr(case))
        
if __name__ == '__main__':
    solve()