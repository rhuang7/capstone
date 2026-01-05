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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        from collections import Counter
        cnt = Counter(A)
        max_len = 0
        min_cost = float('inf')
        for key in cnt:
            if key > max_len:
                max_len = key
        for key in cnt:
            total = 0
            for a in A:
                total += a // key
                if a % key != 0:
                    total += 1
            if total < min_cost:
                min_cost = total
        results.append(f"{max_len} {min_cost}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()