import sys
MOD = 10**9 + 7

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
        S = data[idx + 1]
        idx += 2
        
        len_S = len(S)
        if len_S == 0:
            results.append(0)
            continue
        
        if N < len_S:
            results.append(0)
            continue
        
        # Number of ways to insert len_S characters into N - len_S positions
        # The formula is (N - len_S + len_S) choose (N - len_S) = (N choose (N - len_S)) = (N choose len_S)
        # But since we have 26 letters, it's 26^(N - len_S) * (N choose len_S)
        k = N - len_S
        if k < 0:
            results.append(0)
            continue
        
        # Compute combination (N choose k)
        from math import comb
        try:
            comb_val = comb(N, k)
        except:
            comb_val = 0
        
        # Compute 26^k mod MOD
        power = pow(26, k, MOD)
        
        res = (comb_val * power) % MOD
        results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()