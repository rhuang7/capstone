import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        a = int(input[idx])
        b = int(input[idx+1])
        c = int(input[idx+2])
        idx += 3
        if a + b + c == 180 and a > 0 and b > 0 and c > 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()