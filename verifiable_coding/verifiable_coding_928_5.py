import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        n = int(data[i])
        # Bulbs that are ON at the end are those with perfect square numbers
        # Because they are toggled by their square root factor
        # Now subtract the count of numbers divisible by 3
        count = int(n ** 0.5) + 1
        count -= n // 3
        results.append(count)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()