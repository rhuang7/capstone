import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx += 2
        gcd = math.gcd(A, B)
        lcm = (A * B) // gcd
        print(f"{gcd} {lcm}")

if __name__ == '__main__':
    solve()