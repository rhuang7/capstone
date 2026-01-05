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
        ops = ['&', '&', '&', '&', '&', '&', '&', '&', '&', '&']  # Placeholder, will be replaced
        for op in ops:
            pass
        # Generate all possible operator orders
        from itertools import permutations
        max_val = 0
        for perm in permutations(ops):
            # Evaluate the expression with this permutation
            # Convert to a list of numbers and operators
            values = nums[:]
            operators = perm
            for i in range(len(operators)):
                a = values[i]
                b = values[i + 1]
                op = operators[i]
                if op == '&':
                    res = a & b
                elif op == '|':
                    res = a | b
                else:  # op == '^'
                    res = a ^ b
                values = values[:i] + [res] + values[i + 2:]
            max_val = max(max_val, values[0])
        print(max_val)

if __name__ == '__main__':
    solve()