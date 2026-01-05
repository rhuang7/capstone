import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
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
        # d = total fruits = apples + mangoes + oranges
        # From a + b + c = 2*(apples + mangoes + oranges) => d = (a + b + c) // 2
        # So apples = (a + c - b) // 2
        # mangoes = (a + b - c) // 2
        # oranges = (b + c - a) // 2
        apples = (a + c - b) // 2
        mangoes = (a + b - c) // 2
        oranges = (b + c - a) // 2
        print(apples, mangoes, oranges)

if __name__ == '__main__':
    solve()