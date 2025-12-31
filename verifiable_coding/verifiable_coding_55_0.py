import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            results.append(1)
        else:
            if n % 2 == 0:
                results.append(n // 2)
            else:
                results.append((n - 1) // 2 + 1)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()