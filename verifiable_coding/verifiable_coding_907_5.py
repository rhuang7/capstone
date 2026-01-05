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
                if i == 0 and s[i+1] == 'T':
                    valid = False
                    break
                j = i + 1
                while j < L and s[j] == '.':
                    j += 1
                if j >= L or s[j] != 'T':
                    valid = False
                    break
                i = j + 1
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