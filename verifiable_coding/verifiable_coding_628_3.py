import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        w_pos = s.index('W')
        left = s[:w_pos].count('B')
        right = s[w_pos+1:].count('B')
        total = left + right
        if total == 0:
            print("Chef")
        else:
            if (left + right) % 2 == 1:
                print("Aleksa")
            else:
                print("Chef")

if __name__ == '__main__':
    solve()