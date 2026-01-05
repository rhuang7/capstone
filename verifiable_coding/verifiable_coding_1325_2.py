import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        a = int(input[idx])
        b = int(input[idx+1])
        c = int(input[idx+2])
        d = int(input[idx+3])
        idx += 4
        apple = (a + c - d) // 2
        mango = (a + b - d) // 2
        orange = (b + c - d) // 2
        print(apple, mango, orange)

if __name__ == '__main__':
    solve()