import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    from collections import defaultdict

    # Precompute powers of 2 up to maximum possible length (1000 digits)
    max_len = 1000
    power_of_two = []
    power = 1
    while len(str(power)) <= max_len:
        power_of_two.append(power)
        power *= 2

    for s in cases:
        found = False
        total = 0
        n = len(s)
        # Try all possible lengths of power of two
        for p in power_of_two:
            s_p = str(p)
            if len(s_p) > n:
                continue
            # Check if s_p can be formed by rearranging s
            if sorted(s_p) == sorted(s):
                # Check for leading zero
                if s_p[0] == '0':
                    continue
                total += p
                found = True
        if found:
            print(total % MOD)
        else:
            print(-1)

if __name__ == '__main__':
    solve()