import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    strings = input[1:T+1]

    for s in strings:
        transitions = 0
        for i in range(8):
            if s[i] != s[(i+1)%8]:
                transitions += 1
        if transitions <= 2:
            print("uniform")
        else:
            print("non-uniform")

if __name__ == '__main__':
    solve()