import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = data[1:t+1]
    
    for s in cases:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 2:
                if stack[-2] == 'A' and stack[-1] == 'B':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == 'B' and stack[-1] == 'B':
                    stack.pop()
                    stack.pop()
        print(len(stack))

if __name__ == '__main__':
    solve()