import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        s = data[i]
        transitions = 0
        for j in range(8):
            if s[j] != s[(j + 1) % 8]:
                transitions += 1
        if transitions <= 2:
            print("uniform")
        else:
            print("non-uniform")

if __name__ == '__main__':
    solve()