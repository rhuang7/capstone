import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        # The modular inverse exists if and only if A and B are coprime
        # So we need to compute gcd(A, B)
        L = math.gcd(A, B)
        print(L)

if __name__ == '__main__':
    solve()