import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        n = int(data[i])
        # A bulb is ON if it is toggled an odd number of times, which happens if it has an odd number of divisors.
        # A number has an odd number of divisors if and only if it is a perfect square.
        # So, the number of bulbs that are ON is the number of perfect squares <= n.
        count = int(n**0.5)
        # Subtract the number of perfect squares divisible by 3
        # A number divisible by 3 and a perfect square is a square of a multiple of 3.
        # So, count the number of squares of multiples of 3 up to n.
        # Let x be such that (3x)^2 <= n => x^2 <= n/9 => x <= sqrt(n/9)
        # So, the count is floor(sqrt(n / 9))
        count -= int((n // 9)**0.5)
        results.append(count)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()