import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    brackets = list(map(int, input[1:]))

    stack = []
    alt_depth = 0
    max_paren = 0
    max_brace = 0
    depth = 0
    last_open = {}

    for i, bracket in enumerate(brackets):
        if bracket == 1 or bracket == 3:
            stack.append((bracket, i))
            last_open[bracket] = i
        else:
            if stack:
                top = stack[-1]
                if top[0] == 1 and bracket == 2:
                    max_paren = max(max_paren, i - last_open[1] + 1)
                elif top[0] == 3 and bracket == 4:
                    max_brace = max(max_brace, i - last_open[3] + 1)
                # Check for alternating depth
                if (top[0] == 1 and bracket == 4) or (top[0] == 3 and bracket == 2):
                    alt_depth = max(alt_depth, depth + 1)
                depth -= 1
                stack.pop()
        depth += 1

    print(alt_depth, max_paren, max_brace)

if __name__ == '__main__':
    solve()