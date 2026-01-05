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
        if s.count('H') > 1 and s.count('T') > 1 and s.index('H') > s.index('T'):
            print("Invalid")
            continue
        if s.count('H') == 0 and s.count('T') == 0:
            print("Valid")
            continue
        if s[0] == 'T' or s[-1] == 'H':
            print("Invalid")
            continue
        h_positions = []
        t_positions = []
        for i, c in enumerate(s):
            if c == 'H':
                h_positions.append(i)
            elif c == 'T':
                t_positions.append(i)
        if len(h_positions) != len(t_positions):
            print("Invalid")
            continue
        for i in range(len(h_positions)):
            if t_positions[i] <= h_positions[i]:
                print("Invalid")
                break
        else:
            print("Valid")

if __name__ == '__main__':
    solve()