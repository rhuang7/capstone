import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        num = data[i]
        count = 0
        while num > 0:
            if num % 10 == 4:
                count += 1
            num //= 10
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()