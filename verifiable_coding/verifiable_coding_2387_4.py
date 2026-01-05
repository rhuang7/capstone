import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        s = int(data[i])
        total = 0
        while s > 0:
            total += s
            s = s // 10
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()