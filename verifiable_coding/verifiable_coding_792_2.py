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
        
        # Number of ways to choose a substring to delete
        # Total ways = (N - len_S + 1) * (26^(N - len_S))
        # But we need to subtract the cases where the substring is not a valid one
        # Wait, no. The problem says that after deleting a substring of non-zero length, the remaining string is S.
        # So the length of M must be N, and after deleting a substring, the remaining string is S.
        # So the length of S must be N - k, where k is the length of the deleted substring (k >= 1).
        # So len_S = N - k => k = N - len_S
        # So the deleted substring has length k = N - len_S
        # So the number of ways is (number of ways to choose a substring of length k in M) = (N - k + 1) = (N - (N - len_S) + 1) = len_S + 1
        # But M is a string of length N, and after deleting a substring of length k = N - len_S, the remaining string is S.
        # So M must be such that S is a subsequence of M, and the rest of the characters are deleted.
        # But the problem says that after deleting a substring, the remaining string is S. So the remaining string is exactly S, not a subsequence.
        # So the string M must be such that S is a substring of M, and the rest of the characters are deleted.
        # So M must be S with some characters inserted in between.
        # The number of such strings is equal to the number of ways to insert (N - len_S) characters into S, where each character can be any of the 26 lowercase letters.
        # So the number of such strings is (26^(N - len_S)) * (len_S + 1)
        # But wait, that's not correct. Because inserting (N - len_S) characters into S can be done in (len_S + 1) ways (inserting at the beginning, between each pair of characters, or at the end).
        # So the total number of strings is (len_S + 1) * (26^(N - len_S))
        
        k = N - len_S
        if k < 0:
            results.append(0)
            continue
        
        # Compute 26^k mod MOD
        power = pow(26, k, MOD)
        # Multiply by (len_S + 1)
        ans = (power * (len_S + 1)) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()