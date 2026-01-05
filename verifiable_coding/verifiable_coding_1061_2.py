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
            if op == '^':
                ops[ops.index(op)] = 'xor'
            elif op == '|':
                ops[ops.index(op)] = 'or'
            else:
                ops[ops.index(op)] = 'and'
        ops = ops[1:]
        nums = nums[1:]
        max_val = 0
        from itertools import permutations
        for perm in permutations(ops):
            stack = []
            for i in range(len(nums)):
                if i == 0:
                    stack.append(nums[i])
                else:
                    if perm[i-1] == 'and':
                        stack[-1] &= nums[i]
                    elif perm[i-1] == 'or':
                        stack[-1] |= nums[i]
                    else:
                        stack[-1] ^= nums[i]
            max_val = max(max_val, stack[0])
        print(max_val)

if __name__ == '__main__':
    solve()