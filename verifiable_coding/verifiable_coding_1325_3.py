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
        # Solve the system of equations
        # a = apples + mangoes
        # b = mangoes + oranges
        # c = oranges + apples
        # d = apples + mangoes + oranges
        # From a + b + c = 2*(apples + mangoes + oranges) => apples + mangoes + oranges = (a + b + c) // 2
        # But d is given, so (a + b + c) // 2 must equal d
        # So apples = (a + c - b) // 2
        # mangoes = (a + b - c) // 2
        # oranges = (b + c - a) // 2
        apples = (a + c - b) // 2
        mangoes = (a + b - c) // 2
        oranges = (b + c - a) // 2
        print(f"{apples} {mangoes} {oranges}")

if __name__ == '__main__':
    solve()