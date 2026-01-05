import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    cases = list(map(int, input[1:t+1]))
    
    for n in cases:
        if n == 1:
            print(0)
            continue
        # We want to find the minimum moves to reach sum >= n
        # The optimal strategy is to increase elements as much as possible before appending
        # Let's find the minimal k such that (k*(k+1))/2 + 1 >= n
        # Because each step increases the sum by 1 (increase) or by the value of the element (append)
        # But the optimal is to increase as much as possible
        # So we find the minimal k where sum of first k natural numbers + 1 >= n
        # Which is equivalent to k*(k+1)/2 + 1 >= n
        # So solve k^2 + k + 2 >= 2n
        # Using quadratic formula
        k = math.isqrt(2 * n - 1)
        while k*(k+1)//2 + 1 < n:
            k += 1
        print(k)

if __name__ == '__main__':
    solve()