import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    MOD = 10**9
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        prefix = 0
        count = 0
        seen = set()
        seen.add(0)
        for num in A:
            prefix = (prefix + num) % MOD
            if (prefix) in seen:
                count += 1
            seen.add(prefix)
        print(count)

if __name__ == '__main__':
    solve()