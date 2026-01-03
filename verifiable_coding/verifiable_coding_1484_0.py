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
                stack.append((i, 0))
                i += 1
            elif s[i] == ')':
                if not stack:
                    break
                start, count = stack.pop()
                sub = s[start:i]
                val = 0
                j = 0
                while j < len(sub):
                    if sub[j] == 'x':
                        val += 2
                        j += 1
                    elif sub[j] == 'y':
                        val += 4
                        j += 1
                    elif sub[j] == 'z':
                        val += 10
                        j += 1
                    elif sub[j].isdigit():
                        num = 0
                        while j < len(sub) and sub[j].isdigit():
                            num = num * 10 + int(sub[j])
                            j += 1
                        val *= num
                    else:
                        j += 1
                if stack:
                    stack[-1] = (stack[-1][0], stack[-1][1] + val)
                else:
                    return val
                i += 1
            else:
                if s[i] in 'xyz':
                    val = 2 if s[i] == 'x' else 4 if s[i] == 'y' else 10
                    if stack:
                        stack[-1] = (stack[-1][0], stack[-1][1] + val)
                    else:
                        return val
                elif s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    if stack:
                        stack[-1] = (stack[-1][0], stack[-1][1] * num)
                    else:
                        return num
                i += 1
        return stack[-1][1] if stack else 0
    
    for s in cases:
        print(parse(s))

if __name__ == '__main__':
    solve()