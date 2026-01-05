import sys

def solve():
    import sys
    sys.setrecursionlimit(10000)
    s = sys.stdin.buffer.read().decode().splitlines()
    T = int(s[0])
    for i in range(1, T+1):
        formula = s[i]
        total = 0
        stack = []
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(total)
                total = 0
                i += 1
            elif formula[i] == ')':
                prev = stack.pop()
                total = prev + total
                i += 1
            else:
                if formula[i] in 'xyz':
                    total += 2 if formula[i] == 'x' else 4 if formula[i] == 'y' else 10
                    i += 1
                else:
                    num = 0
                    while i < len(formula) and formula[i].isdigit():
                        num = num * 10 + int(formula[i])
                        i += 1
                    total *= num
        print(total)

if __name__ == '__main__':
    solve()