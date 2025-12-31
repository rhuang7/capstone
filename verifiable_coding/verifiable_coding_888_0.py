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
    
    # Precompute the pattern for T in S
    pattern = []
    for i in range(len_S):
        pattern.append(S[i])
    
    # Precompute the occurrences of T in a string of length n
    # using the KMP algorithm
    def kmp_failure_function(pattern):
        m = len(pattern)
        fail = [0] * m
        j = 1
        while j < m:
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
        n = len(text)
        m = len(pattern)
        j = 0
        count = 0
        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = fail[j-1]
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                count += 1
                j = fail[j-1]
        return count
    
    fail = kmp_failure_function(T)
    
    # Precompute the number of occurrences of T in a string of length n
    # formed by repeating the pattern of S
    # The string for row N is formed by N characters from S repeated cyclically
    # So the string is S[0], S[0], S[0], ... (N times)
    # But since S is repeated cyclically, it's S[0], S[1], S[2], ... S[len_S-1], S[0], S[1], ...
    # So the string for row N is S[0], S[1], ..., S[len_S-1], S[0], S[1], ... (N times)
    # So the string is S repeated (ceil(N / len_S)) times, and take first N characters
    
    # But we can't precompute for all N up to 1e9, so we need to compute on the fly
    
    for N in queries:
        # The string for row N is formed by N characters from S repeated cyclically
        # So the string is S[0], S[1], ..., S[len_S-1], S[0], S[1], ... (N times)
        # So the string is S repeated (ceil(N / len_S)) times, and take first N characters
        # But we can't generate this string directly for large N
        # Instead, we can simulate the KMP search on the pattern
        
        # The string for row N is of length N
        # We can simulate the KMP search on this string
        
        # The string is formed by repeating the pattern of S cyclically
        # So for each position i in the string (0-based), the character is S[i % len_S]
        
        # We can simulate the KMP search on this string
        # Instead of building the string, we can simulate the KMP search on the pattern
        
        # We can simulate the KMP search on the pattern by using the fact that the string is cyclic
        # We can simulate the KMP search by iterating over the positions in the string
        
        # We can simulate the KMP search on the pattern by using the fact that the string is cyclic
        # We can simulate the KMP search by iterating over the positions in the string
        
        # Initialize variables for KMP search
        j = 0
        count = 0
        for i in range(N):
            # Get the character at position i in the string
            char = S[i % len_S]
            # KMP search
            while j > 0 and char != T[j]:
                j = fail[j-1]
            if char == T[j]:
                j += 1
            if j == len_T:
                count += 1
                j = fail[j-1]
        print(count)
    
if __name__ == '__main__':
    solve()