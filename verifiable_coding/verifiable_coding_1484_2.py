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
                if stack:
                    start, count = stack.pop()
                    sub = s[start:i]
                    num = 0
                    if count == 0:
                        num = 1
                    else:
                        num = int(s[i-count:i])
                    val = parse(sub)
                    stack.append((start, val * num))
                i += 1
            else:
                if stack:
                    start, count = stack[-1]
                    stack[-1] = (start, count + 1)
                else:
                    stack.append((i, 0))
                i += 1
        total = 0
        for start, val in stack:
            total += val
        return total
    
    for case in cases:
        s = case.decode()
        result = parse(s)
        print(result)

if __name__ == '__main__':
    solve()