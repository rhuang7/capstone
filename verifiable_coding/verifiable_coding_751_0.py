import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        x = list(map(int, data[idx:idx + n]))
        idx += n
        has_electricity = [i for i in range(n) if s[i] == '1']
        if len(has_electricity) == 0:
            results.append(0)
            continue
        prev = -1
        total = 0
        for i in range(n):
            if s[i] == '1':
                if prev != -1:
                    total += x[i] - x[prev]
                prev = i
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()