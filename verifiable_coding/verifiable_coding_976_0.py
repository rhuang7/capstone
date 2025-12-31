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
    max_len_paren = 0
    max_len_brace = 0

    for i in range(N):
        if brackets[i] == 1 or brackets[i] == 3:
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
                    if length > max_len_brace:
                        max_len_brace = length
                stack.pop()
                current_depth = 0
                if stack:
                    current_depth = 1
                if current_depth > max_depth:
                    max_depth += 1
            else:
                # Mismatch, but input is guaranteed to be well-bracketed
                pass

    print(max_depth, max_len_paren, max_len_brace)

if __name__ == '__main__':
    solve()