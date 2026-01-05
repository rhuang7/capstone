import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        index += 2
        # The modular inverse exists if and only if A and B are coprime
        # So we compute the GCD of A and B
        L = math.gcd(A, B)
        print(L)

if __name__ == '__main__':
    solve()