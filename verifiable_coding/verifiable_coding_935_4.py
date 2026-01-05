import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        X = int(data[i])
        if X == 0:
            results.append(-1)
            continue
        if X % 10 == 0:
            results.append(0)
            continue
        count = 0
        while X % 10 != 0:
            X *= 2
            count += 1
            if X > 10**18:
                results.append(-1)
                break
        else:
            results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()