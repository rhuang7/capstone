import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    from collections import Counter
    from math import log2, pow

    def is_power_of_two(n):
        return (n & (n - 1)) == 0

    def get_power_of_two_candidates(s):
        n = len(s)
        power_of_two_candidates = set()
        for i in range(1, n+1):
            if (1 << i) > 10**n:
                break
            if is_power_of_two(1 << i):
                s_str = str(1 << i)
                if len(s_str) > n:
                    continue
                if sorted(s_str) == sorted(s):
                    power_of_two_candidates.add(1 << i)
        return power_of_two_candidates

    for s in cases:
        candidates = get_power_of_two_candidates(s)
        if not candidates:
            print(-1)
        else:
            total = sum(candidates) % MOD
            print(total)

if __name__ == '__main__':
    solve()