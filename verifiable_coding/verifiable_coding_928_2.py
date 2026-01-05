import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        n = int(data[i])
        # Number of bulbs that are ON after n fluctuations is the number of perfect squares <= n
        # Because a bulb is toggled once for each of its divisors, and only perfect squares have an odd number of divisors
        # Then, we subtract the number of bulbs divisible by 3 (since they are ON and need to be turned off)
        on_bulbs = int(n**0.5)
        # Count numbers <= n divisible by 3
        div3 = n // 3
        # Subtract those that are both perfect squares and divisible by 3
        # A number divisible by 3 and a perfect square is a square of a multiple of 3
        # So count squares of multiples of 3 <= n
        # Let x be such that (3x)^2 <= n => x^2 <= n/9 => x <= sqrt(n/9)
        # So count of such numbers is floor(sqrt(n/9))
        sqrt_n_9 = int((n / 9) ** 0.5)
        # Subtract those that are both perfect squares and divisible by 3
        on_bulbs -= sqrt_n_9
        results.append(on_bulbs)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()