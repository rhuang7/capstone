import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    brackets = list(map(int, input[1:]))

    stack = []
    depth = 0
    max_depth = 0
    max_len_paren = 0
    max_len_bracket = 0

    for i in range(N):
        if brackets[i] in (1, 3):
            stack.append((brackets[i], i))
        else:
            if not stack:
                continue
            top = stack[-1]
            if (top[0] == 1 and brackets[i] == 2) or (top[0] == 3 and brackets[i] == 4):
                # Match found
                start = top[1]
                end = i
                length = end - start + 1
                if top[0] == 1:
                    if length > max_len_paren:
                        max_len_paren = length
                else:
                    if length > max_len_bracket:
                        max_len_bracket = length
                stack.pop()
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                # Mismatch, but input is guaranteed to be well-bracketed
                pass

    print(max_depth, max_len_paren, max_len_bracket)

if __name__ == '__main__':
    solve()