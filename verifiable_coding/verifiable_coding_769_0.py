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
        # The largest number that divides both A and B is their GCD
        # But for the modular inverse to exist, A and B must be coprime
        # So we need to check if GCD(A, B) is 1
        g = math.gcd(A, B)
        if g == 1:
            print(1)
        else:
            print(g)

if __name__ == '__main__':
    solve()