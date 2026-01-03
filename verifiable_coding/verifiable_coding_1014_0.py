import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    from collections import defaultdict

    # Precompute powers of 2 up to 10^1000 (since max length is 1000)
    # We'll store them as strings to compare with the input strings
    powers_of_2 = []
    power = 1
    while len(str(power)) <= 1000:
        powers_of_2.append(str(power))
        power *= 2

    for s in cases:
        found = False
        total = 0
        for p in powers_of_2:
            if len(p) > len(s):
                continue
            if len(p) == len(s):
                if sorted(p) == sorted(s):
                    total = (total + int(p)) % MOD
                    found = True
        if found:
            print(total)
        else:
            print(-1)

if __name__ == '__main__':
    solve()