import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        S = data[idx]
        idx += 1
        queries = []
        for __ in range(Q):
            L = int(data[idx]) - 1
            R = int(data[idx+1]) - 1
            queries.append((L, R))
            idx += 2
        
        for L, R in queries:
            # Check if there is a rich substring in the range [L, R]
            # A rich substring must have length >= 3
            # For a substring to be rich, there must be a character that appears more than half the length
            # We can check for each possible substring of length 3, 4, ..., up to R-L+1
            # However, this is too slow for large N and Q
            # Instead, we can check if there exists a character that appears more than half the length of the substring
            # For a substring of length L, a character must appear at least (L // 2 + 1) times
            # So for the entire range [L, R], we can check if any character appears more than half the length of the substring
            # We can precompute prefix sums for each character
            # Then, for each query, we can check for each character if it appears more than half the length of the substring
            # The substring length is R - L + 1
            # So for each query, we check if any character appears more than (R - L + 1) // 2 times in the substring
            # We can do this efficiently using prefix sums
            # Precompute prefix sums for each character
            # For each character c in 'a' to 'z', prefix[c][i] is the number of times c appears in S[0..i-1]
            # Then, for a query [L, R], the count of c is prefix[c][R+1] - prefix[c][L]
            # We can check for each character if this count is > (R - L + 1) // 2
            # If any character satisfies this, then the answer is YES, else NO
            
            # Precompute prefix sums
            prefix = [ [0]*(N+1) for _ in range(26) ]
            for i in range(N):
                for c in range(26):
                    prefix[c][i+1] = prefix[c][i]
                c = ord(S[i]) - ord('a')
                prefix[c][i+1] += 1
            
            length = R - L + 1
            if length < 3:
                results.append("NO")
                continue
            half = (length) // 2
            found = False
            for c in range(26):
                cnt = prefix[c][R+1] - prefix[c][L]
                if cnt > half:
                    found = True
                    break
            results.append("YES" if found else "NO")
    
    print('\n'.join(results))