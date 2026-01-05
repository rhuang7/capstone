import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    from collections import Counter

    def is_power_of_two(n):
        return (n & (n - 1)) == 0

    def get_powers_of_two_up_to_max_len(max_len):
        powers = []
        current = 1
        while True:
            if len(str(current)) > max_len:
                break
            powers.append(current)
            current <<= 1
        return powers

    for s in cases:
        n = len(s)
        if n == 1:
            print(-1)
            continue
        max_len = n
        powers = get_powers_of_two_up_to_max_len(max_len)
        total = 0
        for power in powers:
            s_str = str(power)
            if len(s_str) > n:
                continue
            if len(s_str) < n:
                continue
            if len(s_str) == n:
                if s == s_str:
                    total += power
        if total == 0:
            print(-1)
        else:
            print(total % MOD)

if __name__ == '__main__':
    solve()