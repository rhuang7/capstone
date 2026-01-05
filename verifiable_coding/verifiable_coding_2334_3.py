import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = data[1:t+1]
    
    for s in cases:
        stack = []
        for c in s:
            if stack and stack[-1] == 'B' and c == 'B':
                stack.pop()
            elif stack and stack[-1] == 'A' and c == 'B':
                stack.pop()
            else:
                stack.append(c)
        print(len(stack))

if __name__ == '__main__':
    solve()