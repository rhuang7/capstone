import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        count = 0
        for d in range(1, 10):
            num = 0
            for j in range(1, 10):
                num = num * 10 + d
                if num > n:
                    break
                count += 1
        results.append(count)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()