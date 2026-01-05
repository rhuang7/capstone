import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0]
    T = data[1]
    Q = int(data[2])
    queries = list(map(int, data[3:3+Q]))
    
    len_S = len(S)
    len_T = len(T)
    
    # Precompute the positions where T occurs in S
    # We'll use a sliding window approach to find all occurrences of T in S
    # But since S can be large, we need an efficient way
    # We'll use the Knuth-Morris-Pratt (KMP) algorithm for pattern matching
    def kmp_failure_function(pattern):
        fail = [0] * len(pattern)
        j = 1
        while j < len(pattern):
            if pattern[j] == pattern[fail[j]]:
                fail[j] = fail[j-1] + 1
                j += 1
            else:
                if fail[j-1] == 0:
                    fail[j] = 0
                    j += 1
                else:
                    j = fail[j-1]
        return fail
    
    def kmp_search(text, pattern, fail):
        j = 0
        i = 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
                if j == len(pattern):
                    yield i - j
                    j = fail[j-1]
            else:
                if j != 0:
                    j = fail[j-1]
                else:
                    i += 1
    
    fail_T = kmp_failure_function(T)
    occurrences_in_S = list(kmp_search(S, T, fail_T))
    
    # Now, for each query N, we need to find the number of occurrences of T in the N-th row
    # The N-th row is formed by repeating the string S cyclically, with N characters
    # So the row is S[0], S[0]S[1], S[0]S[1]S[2], ... until N characters
    # So the row is S[0] * (N // len_S) + S[0:N % len_S]
    # But we need to find how many times T appears in this string
    # We can precompute the positions of T in S and then compute how many times they appear in the row
    
    # Precompute the positions of T in S
    # We'll use the occurrences_in_S list
    # Now, for a row of length N, the row is formed by repeating S cyclically
    # So the row is S[0] * (N // len_S) + S[0:N % len_S]
    # The total number of characters in the row is N
    
    # For each query N, we need to find the number of occurrences of T in this row
    
    # Let's precompute the positions of T in S
    # We'll create a list of all positions where T occurs in S
    # Then, for a row of length N, we can compute how many times T appears in it
    # We'll use the occurrences_in_S list to find how many times T appears in the row
    
    # Now, for a given N, the row is formed by repeating S cyclically
    # So the row is S[0] * (N // len_S) + S[0:N % len_S]
    # The total length is N
    
    # We can compute how many times T appears in this row
    # We'll use the occurrences_in_S list and the cyclic nature of the row
    
    # For each query N:
    # - Compute the number of full cycles of S in the row: full_cycles = N // len_S
    # - Compute the remainder: rem = N % len_S
    # - The row is S[0] * full_cycles + S[0:rem]
    # - Now, we need to find how many times T appears in this row
    
    # We'll precompute the positions where T occurs in S
    # For each occurrence in S, we can compute how many times it appears in the row
    # Each occurrence in S can be part of the row in multiple ways
    
    # For example, if T occurs at position i in S, then in the row, it can be part of the full cycles and the remainder
    
    # So, for each occurrence in S, we can compute how many times it appears in the row
    
    # Let's precompute the positions of T in S
    # We'll create a list of all positions where T occurs in S
    # Then, for a row of length N, we can compute how many times T appears in it
    
    # For each occurrence in S, we can compute how many times it appears in the row
    
    # Let's precompute the positions of T in S
    # We'll create a list of all positions where T occurs in S
    # For example, if S is "abcabc", and T is "abc", then the positions are 0, 3
    
    # Now, for each query N:
    # - Compute the number of full cycles: full_cycles = N // len_S
    # - Compute the remainder: rem = N % len_S
    # - The row is S[0] * full_cycles + S[0:rem]
    # - The total length is N
    
    # Now, we need to find how many times T appears in this row
    
    # For each occurrence in S, we can compute how many times it appears in the row
    
    # Let's precompute the positions of T in S
    # For each occurrence in S, we can compute how many times it appears in the row
    
    # Now, for each query N:
    # - Compute the number of full cycles: full_cycles = N // len_S
    # - Compute the remainder: rem = N % len_S
    # - The row is S[0] * full_cycles + S[0:rem]
    # - The total length is N
    
    # Now, we need to find how many times T appears in this row
    
    # For each occurrence in S, we can compute how many times it appears in the row
    
    # Let's precompute the positions of T in S
    # For each occurrence in S, we can compute how many times it appears in the row
    
    # Let's compute the answer for each query
    
    for N in queries:
        len_row = N
        len_S = len(S)
        len_T = len(T)
        
        if len_T > len_row:
            print(0)
            continue
        
        full_cycles = N // len_S
        rem = N % len_S
        
        # The row is S[0] * full_cycles + S[0:rem]
        # We need to find how many times T appears in this row
        
        # We'll use the occurrences_in_S list to find how many times T appears in the row
        
        # For each occurrence in S, we can compute how many times it appears in the row
        # Each occurrence in S can be part of the full cycles and the remainder
        
        # Let's compute how many times T appears in the row
        count = 0
        
        # For the full cycles
        for pos in occurrences_in_S:
            # The occurrence starts at pos and ends at pos + len_T - 1
            # In the full cycles, this occurrence can appear full_cycles times
            # But we need to check if the occurrence is within the full cycles
            # The full cycles are of length len_S
            # So, the occurrence can be in the full cycles if pos + len_T - 1 < len_S
            if pos + len_T - 1 < len_S:
                count += full_cycles
        
        # For the remainder
        # The remainder is the first rem characters of S
        # We need to check if T appears in this part
        # We can use the KMP algorithm again to find occurrences in the remainder
        # But since rem can be up to len_S, which is up to 1e5, and Q is up to 1e5, this is not efficient
        
        # So we'll precompute all occurrences of T in S, and then for each occurrence, check if it is within the remainder
        
        # For the remainder
        for pos in occurrences_in_S:
            # The occurrence starts at pos and ends at pos + len_T - 1
            # In the remainder, this occurrence can be present if pos + len_T - 1 < rem
            if pos + len_T - 1 < rem:
                count += 1
        
        print(count)
    
if __name__ == '__main__':
    solve()