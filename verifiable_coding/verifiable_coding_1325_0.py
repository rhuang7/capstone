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
        # a + b = apples + mangoes
        # b + c = mangoes + oranges
        # c + a = oranges + apples
        # a + b + c = d
        # From the first three equations, we can find apples, mangoes, oranges
        apples = (a + c - d) // 2
        mangoes = (a + b - d) // 2
        oranges = (b + c - d) // 2
        print(apples, mangoes, oranges)

if __name__ == '__main__':
    solve()