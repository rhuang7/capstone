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
        nums = [int(n) for n in nums]
        ops = [op for op in ops]
        n = len(ops)
        # Try all possible operator orders
        from itertools import permutations
        max_val = 0
        for perm in permutations(ops):
            # Apply the operators in the given order
            # Start with the first number
            res = nums[0]
            for i in range(n):
                op = perm[i]
                next_num = nums[i + 1]
                if op == '&':
                    res &= next_num
                elif op == '|':
                    res |= next_num
                elif op == '^':
                    res ^= next_num
            max_val = max(max_val, res)
        print(max_val)

if __name__ == '__main__':
    solve()