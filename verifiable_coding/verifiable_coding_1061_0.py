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
        nums = [int(x) for x in nums]
        ops = [x for x in ops]
        
        from itertools import permutations
        
        max_val = 0
        n = len(ops)
        for perm in permutations(ops):
            expr = nums[0]
            for i in range(n):
                op = perm[i]
                num = nums[i+1]
                if op == '&':
                    expr &= num
                elif op == '|':
                    expr |= num
                elif op == '^':
                    expr ^= num
            max_val = max(max_val, expr)
        return max_val
    
    for case in cases:
        print(max_expr(case))
        
if __name__ == '__main__':
    solve()