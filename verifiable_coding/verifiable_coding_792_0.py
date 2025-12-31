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
        
        # The number of possible strings is (26^len_S) * (26^(N - len_S)) - (26^len_S - 1) * (26^(N - len_S - 1))
        # But we need to compute it correctly based on the problem statement
        
        # The correct formula is (26^len_S) * (26^(N - len_S)) - (26^len_S - 1) * (26^(N - len_S - 1))
        # This is because we subtract the cases where the substring is not deleted (i.e., the original string is kept)
        
        # But we need to compute it correctly based on the problem statement
        # The correct formula is (26^len_S) * (26^(N - len_S)) - (26^len_S - 1) * (26^(N - len_S - 1))
        
        # Precompute powers of 26 modulo MOD
        max_pow = max(len_S, N - len_S)
        pow_26 = [1] * (max_pow + 1)
        for i in range(1, max_pow + 1):
            pow_26[i] = (pow_26[i - 1] * 26) % MOD
        
        len_S_pow = pow_26[len_S]
        N_lenS_pow = pow_26[N - len_S]
        len_S_minus_1_pow = pow_26[len_S - 1]
        N_lenS_minus_1_pow = pow_26[N - len_S - 1]
        
        term1 = (len_S_pow * N_lenS_pow) % MOD
        term2 = ((len_S_minus_1_pow * N_lenS_minus_1_pow) % MOD)
        ans = (term1 - term2) % MOD
        
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()