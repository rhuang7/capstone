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
        if L != len(s):
            print("Invalid")
            continue
        i = 0
        valid = True
        while i < L:
            if s[i] == 'H':
                h_pos = i
                i += 1
                while i < L and s[i] == '.':
                    i += 1
                if i >= L or s[i] != 'T':
                    valid = False
                    break
                i += 1
            elif s[i] == 'T':
                valid = False
                break
            else:
                i += 1
        if valid and i == L:
            print("Valid")
        else:
            print("Invalid")

if __name__ == '__main__':
    solve()