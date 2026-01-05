import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    q = int(data[0])
    index = 1
    results = []
    for _ in range(q):
        n = int(data[index])
        m = int(data[index+1])
        index += 2
        if m == 0:
            results.append(0)
            continue
        total = 0
        for i in range(1, n+1, m):
            last_digit = i % 10
            total += last_digit
        results.append(total)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()