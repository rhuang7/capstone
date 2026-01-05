import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    brackets = data[1:]

    stack = []
    alt_depth = 0
    max_paren = 0
    max_bracket = 0
    depth = 0
    last_open = {}

    for i, b in enumerate(brackets):
        if b == 1 or b == 3:
            stack.append((b, i))
            last_open[b] = i
        else:
            if stack:
                top = stack[-1]
                if top[0] == 1 and b == 2:
                    if depth > 0:
                        alt_depth = max(alt_depth, depth)
                    depth -= 1
                    max_paren = max(max_paren, i - last_open[1] + 1)
                elif top[0] == 3 and b == 4:
                    if depth > 0:
                        alt_depth = max(alt_depth, depth)
                    depth -= 1
                    max_bracket = max(max_bracket, i - last_open[3] + 1)
                stack.pop()

    print(alt_depth, max_paren, max_bracket)

if __name__ == '__main__':
    solve()