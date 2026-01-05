import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        n = int(data[i])
        # A bulb is ON if it is toggled an odd number of times
        # This happens if the number of divisors of the bulb's number is odd
        # Which is true only for perfect squares
        count = int(n ** 0.5)
        # Subtract the number of bulbs divisible by 3
        count -= n // 3
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()