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
        if s.count('H') > 1 and s.count('T') > 1 and s.count('T') < s.count('H'):
            print("Invalid")
            continue
        if s[0] == 'T' or s[-1] == 'H':
            print("Invalid")
            continue
        h_pos = -1
        t_pos = -1
        for i, c in enumerate(s):
            if c == 'H':
                if h_pos != -1:
                    print("Invalid")
                    break
                h_pos = i
            elif c == 'T':
                if t_pos != -1 or h_pos == -1:
                    print("Invalid")
                    break
                t_pos = i
        else:
            if h_pos == -1 or t_pos == -1:
                print("Valid")
            else:
                print("Valid")
        continue
    return

if __name__ == '__main__':
    solve()