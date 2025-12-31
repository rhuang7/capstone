import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    mod = 8589934592

    def compute_min_toggles(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 3
        # For n >= 3, the pattern is (n * (n + 1)) // 2
        return (n * (n + 1)) // 2

    for i in range(T):
        n = cases[i]
        res = compute_min_toggles(n)
        print(f"Case {i+1}: {res % mod}")

if __name__ == '__main__':
    solve()