import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    for n in cases:
        if n == 1:
            print(1)
        else:
            # The minimum time is the smallest integer k such that k*(k+1)/2 >= n
            # This is equivalent to finding the smallest k where k^2 + k - 2n >= 0
            k = math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)
            print(k)

if __name__ == '__main__':
    solve()