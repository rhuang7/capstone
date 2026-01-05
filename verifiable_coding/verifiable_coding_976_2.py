import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    brackets = data[1:]

    stack = []
    alt_depth = 0
    max_len_paren = 0
    max_len_bracket = 0
    depth = 0
    prev = -1

    for i in range(N):
        if brackets[i] == 1 or brackets[i] == 3:
            stack.append((brackets[i], i))
            depth += 1
        else:
            if stack:
                top = stack[-1]
                if (top[0] == 1 and brackets[i] == 2) or (top[0] == 3 and brackets[i] == 4):
                    if depth > 1:
                        alt_depth = max(alt_depth, depth - 1)
                    if top[0] == 1:
                        max_len_paren = max(max_len_paren, i - top[1] + 1)
                    else:
                        max_len_bracket = max(max_len_bracket, i - top[1] + 1)
                    stack.pop()
                    depth -= 1
                else:
                    # This should not happen as input is well-bracketed
                    pass

    print(alt_depth, max_len_paren, max_len_bracket)

if __name__ == '__main__':
    solve()