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
                num = 0
                if count == 0:
                    num = 1
                else:
                    num = int(s[i-count:i])
                val = 0
                j = 0
                while j < len(sub):
                    if sub[j] == 'x':
                        val += 2 * num
                        j += 1
                    elif sub[j] == 'y':
                        val += 4 * num
                        j += 1
                    elif sub[j] == 'z':
                        val += 10 * num
                        j += 1
                    else:
                        j += 1
                stack.append((start, val))
                i += 1
            else:
                i += 1
        return stack[0][1]
    
    for case in cases:
        if case:
            print(parse(case))

if __name__ == '__main__':
    solve()