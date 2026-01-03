import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    brackets = list(map(int, data[1:]))

    stack = []
    alt_depth = 0
    max_paren = 0
    max_bracket = 0
    depth = 0
    current_alt = 0

    for i in range(N):
        if brackets[i] in [1, 3]:
            stack.append((brackets[i], i))
            depth += 1
            current_alt = 0
        else:
            if not stack:
                continue
            top = stack[-1]
            if top[0] == 1 and brackets[i] == 2:
                if depth > 1:
                    current_alt = max(current_alt, 1)
                if i - top[1] + 1 > max_paren:
                    max_paren = i - top[1] + 1
            elif top[0] == 3 and brackets[i] == 4:
                if depth > 1:
                    current_alt = max(current_alt, 1)
                if i - top[1] + 1 > max_bracket:
                    max_bracket = i - top[1] + 1
            stack.pop()
            depth -= 1
            if depth > 0:
                current_alt = max(current_alt, 1)
            alt_depth = max(alt_depth, current_alt)

    print(alt_depth, max_paren, max_bracket)

if __name__ == '__main__':
    solve()