import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        C = int(input[idx+2])
        idx += 3
        if A + B + C == 180 and A > 0 and B > 0 and C > 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()