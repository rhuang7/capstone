import sys

def solve():
    import sys
    sys.setrecursionlimit(10000)
    S = sys.stdin.buffer.read().decode().splitlines()
    T = int(S[0])
    for i in range(1, T+1):
        s = S[i]
        total = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(total)
                total = 0
                i += 1
            elif s[i] == ')':
                multiplier = 1
                i += 1
                while i < len(s) and s[i].isdigit():
                    multiplier = multiplier * 10 + int(s[i])
                    i += 1
                total = total * multiplier
                if stack:
                    total += stack.pop()
                else:
                    total = total * multiplier
            else:
                if s[i] in 'xyz':
                    total += 2 if s[i] == 'x' else 4 if s[i] == 'y' else 10
                i += 1
        print(total)

if __name__ == '__main__':
    solve()