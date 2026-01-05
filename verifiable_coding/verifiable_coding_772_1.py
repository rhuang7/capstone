import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        N = len(S)
        count = 0
        
        # Each single element is a valid exponential sequence
        count += N
        
        # For sequences of length >= 2
        # We need to find all exponential sequences and check if they form a palindrome
        # An exponential sequence is of the form i1, i2, ..., ik where ij+1 = p * ij for some p > 1
        # So for each position i, we can try to find all j such that j = i * p for some p > 1
        # And check if the sequence from i to j forms a palindrome
        
        # We can use memoization to avoid recomputing
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # For each position i, we try to find all j = i * p for p > 1
        # And check if the sequence from i to j is a palindrome
        for i in range(N):
            current = S[i]
            count += 1  # single element is already counted
            # Try all possible p > 1
            p = 2
            while True:
                j = i * p
                if j >= N:
                    break
                # Check if the sequence from i to j is a palindrome
                if is_palindrome(S, i, j):
                    count += 1
                p += 1
        
        print(count)

if __name__ == '__main__':
    solve()