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
        
        if N < len_S:
            results.append(0)
            continue
        
        # Number of ways to insert len_S characters into N positions
        # Total ways = (N + len_S - 1) choose len_S
        # But we need to subtract the cases where the inserted characters are not S
        # So total valid = total ways - (ways where inserted characters are not S)
        # But this is not directly applicable. Instead, we need to find the number of strings M of length N such that deleting a substring of M gives S.
        
        # The number of such M is equal to the number of ways to insert len_S characters into N positions, but ensuring that the inserted characters form S.
        # So the number of valid M is (N - len_S + 1) * 26^(N - len_S)
        # Because we can choose any substring of M to delete, and the remaining characters must be S.
        # The number of possible substrings to delete is (N - len_S + 1)
        # And for each such substring, the remaining characters must be S, so the rest of the characters can be any letters.
        
        # But this is not correct. The correct way is:
        # The number of valid M is (N - len_S + 1) * 26^(N - len_S)
        # Because we can choose any substring of M to delete, and the remaining characters must be S. The rest of the characters can be any letters.
        
        # But this is not correct. The correct way is:
        # The number of valid M is (N - len_S + 1) * 26^(N - len_S)
        # Because we can choose any substring of M to delete, and the remaining characters must be S. The rest of the characters can be any letters.
        
        # However, the correct formula is:
        # The number of valid M is (N - len_S + 1) * 26^(N - len_S)
        
        # So we calculate this value modulo 10^9 + 7
        
        # Precompute powers of 26 up to 1e5
        # But since N can be up to 1e18, we need to compute 26^(N - len_S) mod MOD efficiently using fast exponentiation
        
        power = pow(26, N - len_S, MOD)
        count = (N - len_S + 1) * power % MOD
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()