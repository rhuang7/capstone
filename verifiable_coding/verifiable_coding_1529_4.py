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
        L = list(map(int, data[idx:idx+N]))
        idx += N
        digits = list(map(str, L))
        from itertools import permutations
        total = 0
        for p in permutations(digits):
            num = int(''.join(p))
            total += num
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()