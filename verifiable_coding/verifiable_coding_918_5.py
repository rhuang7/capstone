import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    mod = 8589934592

    results = []
    for i, n in enumerate(cases, 1):
        if n == 0:
            results.append(f"Case {i}: 0")
            continue
        # For n >= 1, the minimum number of toggle is (n * (n + 1)) // 2
        # But we need to handle large n efficiently
        # Using formula: (n * (n + 1)) // 2 mod 2^33
        res = (n * (n + 1) // 2) % mod
        results.append(f"Case {i}: {res}")

    print('\n'.join(results))

if __name__ == '__main__':
    solve()