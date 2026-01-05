import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        a, b, c, d = map(int, input[idx:idx+4])
        idx += 4
        if a == 0 or b == 0 or c == 0 or d == 0:
            print("Yes")
        else:
            if (a + b == 0 or a + c == 0 or a + d == 0 or
                b + c == 0 or b + d == 0 or
                c + d == 0):
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    solve()