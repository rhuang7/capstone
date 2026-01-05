import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        if len(s) != 5:
            print("Error")
            continue
        if s[0].islower() and s[0] >= 'a' and s[0] <= 'h' and s[2] == '-' and s[3].isdigit() and s[3] >= '1' and s[3] <= '8' and s[4].islower() and s[4] >= 'a' and s[4] <= 'h' and s[1].isdigit() and s[1] >= '1' and s[1] <= '8' and s[3].isdigit() and s[3] >= '1' and s[3] <= '8':
            x1 = ord(s[0]) - ord('a')
            y1 = int(s[1]) - 1
            x2 = ord(s[3]) - ord('a')
            y2 = int(s[4]) - 1
            if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
                print("Yes")
            else:
                print("No")
        else:
            print("Error")

if __name__ == '__main__':
    solve()