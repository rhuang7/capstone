import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        if n == 1:
            print(-1)
            continue
        
        # Precompute all powers of 2 up to 10^1000 (since max length is 1000)
        max_len = 1000
        powers_of_2 = []
        power = 1
        while len(str(power)) <= max_len:
            powers_of_2.append(power)
            power <<= 1
        
        # Check each power of 2
        total = 0
        for p in powers_of_2:
            s_p = str(p)
            if len(s_p) > n:
                continue
            if sorted(s_p) == sorted(s):
                total += p
        
        if total == 0:
            print(-1)
        else:
            print(total % MOD)

if __name__ == '__main__':
    solve()