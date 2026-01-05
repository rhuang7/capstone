import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    brackets = data[1:]
    
    stack = []
    depth = 0
    max_depth = 0
    max_paren = 0
    max_brace = 0
    prev = -1
    
    for i in range(N):
        if brackets[i] == 1 or brackets[i] == 3:
            stack.append((brackets[i], i))
        else:
            if stack:
                op, pos = stack.pop()
                if op == 1:
                    if prev == 3:
                        depth += 1
                    elif prev == 4:
                        depth -= 1
                    max_depth = max(max_depth, depth)
                    max_paren = max(max_paren, i - pos + 1)
                    prev = 1
                elif op == 3:
                    if prev == 1:
                        depth += 1
                    elif prev == 2:
                        depth -= 1
                    max_depth = max(max_depth, depth)
                    max_brace = max(max_brace, i - pos + 1)
                    prev = 3
    print(max_depth, max_paren, max_brace)

if __name__ == '__main__':
    solve()