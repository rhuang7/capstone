import sys

def solve():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.buffer.read().split(b'\n')
    T = int(data[0])
    cases = data[1:T+1]
    
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
                if s[i] in 'xyz':
                    stack.append(2 if s[i] == 'x' else 4 if s[i] == 'y' else 10)
                    i += 1
                else:
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    if stack:
                        stack[-1] = stack[-1] * num
                    else:
                        stack.append(num)
        return sum(stack)
    
    for case in cases:
        print(parse(case))

if __name__ == '__main__':
    solve()