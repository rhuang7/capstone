import sys

def solve():
    import sys
    sys.setrecursionlimit(10000)
    T = int(sys.stdin.buffer.read().split()[0])
    cases = sys.stdin.buffer.read().split()[1:]
    
    def parse(s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(0)
                i += 1
            elif s[i] == ')':
                val = stack.pop()
                if stack:
                    stack[-1] = stack[-1] * val
                else:
                    stack.append(val)
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if num == 0:
                    num = 1
                if s[i] == 'x':
                    stack.append(2 * num)
                    i += 1
                elif s[i] == 'y':
                    stack.append(4 * num)
                    i += 1
                elif s[i] == 'z':
                    stack.append(10 * num)
                    i += 1
        return sum(stack)
    
    for s in cases:
        print(parse(s))

if __name__ == '__main__':
    solve()