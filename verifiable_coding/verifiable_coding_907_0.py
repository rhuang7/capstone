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
        if s.count('H') != s.count('T'):
            print("Invalid")
            continue
        snakes = []
        i = 0
        while i < len(s):
            if s[i] == 'H':
                j = i + 1
                while j < len(s) and s[j] == '.':
                    j += 1
                if j >= len(s) or s[j] != 'T':
                    print("Invalid")
                    break
                snakes.append((i, j))
                i = j + 1
            else:
                i += 1
        else:
            valid = True
            for i in range(len(snakes)):
                if i > 0 and snakes[i][0] < snakes[i-1][1]:
                    valid = False
                    break
            if valid:
                print("Valid")
            else:
                print("Invalid")
                
if __name__ == '__main__':
    solve()