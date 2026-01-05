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
        # Total ways = (N + 1) * (N) // 2 - (len_S + 1) * len_S // 2
        # But we need to subtract the cases where the remaining string is S
        # So total valid ways = total ways - (number of ways to delete a substring such that remaining is S)
        
        # Total ways to delete a substring of non-zero length
        total_ways = (N * (N + 1) // 2) - (len_S * (len_S + 1) // 2)
        
        # Number of ways to delete a substring such that remaining is S
        # This is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring that is not in S
        # But this is not correct, we need to find the number of ways to delete a substring such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # So we need to find the number of ways to delete a substring from M such that the remaining is S
        # Which is equal to the number of ways to choose a substring to delete from M such that the remaining is S
        # So the number of such ways is (len_S + 1) * (len_S + 2) // 2 - (len_S + 1) * len_S // 2
        # Which is (len_S + 1)
        
        # The number of ways to delete a substring such that the remaining is S is (len_S + 1)
        # Because we can delete any prefix, any suffix, or any substring in between
        # So the number of such ways is (len_S + 1)
        
        # So the answer is total_ways - (len_S + 1)
        ans = (total_ways - (len_S + 1)) % MOD
        results.append(ans)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()