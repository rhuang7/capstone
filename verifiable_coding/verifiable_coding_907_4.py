import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    R = int(input[idx])
    idx += 1
    for _ in range(R):
        L = int(input[idx])
        idx += 1
        s = input[idx]
        idx += 1
        i = 0
        in_snake = False
        snakes = []
        while i < L:
            if s[i] == 'H':
                if in_snake:
                    print("Invalid")
                    break
                in_snake = True
                start = i
                i += 1
                while i < L and s[i] == '.':
                    i += 1
                if i >= L or s[i] != 'T':
                    print("Invalid")
                    break
                snakes.append((start, i))
                in_snake = False
            elif s[i] == 'T':
                print("Invalid")
                break
            else:
                i += 1
        else:
            if in_snake:
                print("Invalid")
            else:
                print("Valid")

if __name__ == '__main__':
    solve()