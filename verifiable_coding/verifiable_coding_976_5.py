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
    paren_stack = []
    bracket_stack = []

    for i in range(N):
        bracket = brackets[i]
        if bracket == 1 or bracket == 3:
            stack.append((bracket, i))
            if bracket == 1:
                paren_stack.append(i)
            else:
                bracket_stack.append(i)
        else:
            last = stack.pop()
            if last[0] == 1:
                # Matching )
                start = paren_stack.pop()
                length = i - start + 1
                max_len_paren = max(max_len_paren, length)
            else:
                # Matching ]
                start = bracket_stack.pop()
                length = i - start + 1
                max_len_bracket = max(max_len_bracket, length)
            # Check for alternating depth
            if stack and (last[0] == 1 and stack[-1][0] == 3 or last[0] == 3 and stack[-1][0] == 1):
                alt_depth += 1

    print(alt_depth, max_len_paren, max_len_bracket)

if __name__ == '__main__':
    solve()