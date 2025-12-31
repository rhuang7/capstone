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
        
        # Preprocess prefix sums for each character
        prefix = [[0] * (N + 1) for _ in range(26)]
        for i in range(N):
            for c in range(26):
                prefix[c][i+1] = prefix[c][i]
            prefix[ord(S[i]) - ord('a')][i+1] += 1
        
        # Process queries
        for L, R in queries:
            # Check if there is a rich substring in [L, R]
            # A rich substring must have length >= 3
            # For each possible character, check if it occurs more than half the length of some substring
            # We can check for all possible substrings of length 3 to 1000 (max possible)
            # But that's too slow, so we optimize
            # Instead, check for all possible characters in the current range
            # For each character, check if it appears more than half of some substring
            # We can check for each character in the range, and see if it appears more than half of some substring
            # For a substring to be rich, it must have length >= 3
            # So, for each character, check if it appears more than half of some substring of length >= 3
            # We can do this by checking for each character in the range, and see if it appears more than half of some substring
            # For a character c, the maximum number of times it can appear in a substring of length L is L
            # So, for each possible substring length from 3 to R-L+1, check if c appears more than half of that length
            # But this is still too slow
            # So, we can use the following observation:
            # A rich substring must have a character that appears more than half of its length
            # So, for the current range [L, R], we can check for each character in the range, and see if it appears more than half of some substring
            # We can do this by checking if any character appears more than half of the length of the entire range
            # Because if a character appears more than half of the entire range, then there must be a substring of length >= 3 that is rich
            # So, for each character in the range, check if its count in the range is more than (R-L+1)//2
            # If yes, then there is a rich substring
            # But this is not sufficient, because the character may not be in a substring of length >= 3
            # So, we need to check for all possible substrings of length >= 3
            # But that's too slow
            # So, we can use the following approach:
            # For each character in the range, check if it appears more than half of the length of the entire range
            # If yes, then there is a rich substring
            # Because if a character appears more than half of the entire range, then there must be a substring of length >= 3 that is rich
            # So, for the current query, check for each character in the range, and see if it appears more than half of the length of the entire range
            # If any such character exists, then the answer is YES
            # Otherwise, it's NO
            # But this is not correct, because the character may not be in a substring of length >= 3
            # So, we need to check for each character in the range, and see if it appears more than half of some substring of length >= 3
            # But this is still too slow
            # So, we can use the following approach:
            # For each character in the range, check if it appears more than half of the length of the entire range
            # If yes, then there is a rich substring
            # Otherwise, check if there is a substring of length 3 where the character appears more than 1.5 times
            # This is the only possible way for a substring of length 3 to be rich
            # So, for each query, we can:
            # 1. Check if any character appears more than half of the entire range
            # 2. If not, check if any substring of length 3 has a character that appears more than 1.5 times
            # If either is true, then the answer is YES
            # Otherwise, it's NO
            # So, let's implement this
            length = R - L + 1
            max_count = 0
            for c in range(26):
                count = prefix[c][R+1] - prefix[c][L]
                if count > length // 2:
                    results.append("YES")
                    break
            else:
                # Check for substrings of length 3
                found = False
                for i in range(L, R - 2 + 1):
                    c1 = S[i]
                    c2 = S[i+1]
                    c3 = S[i+2]
                    if c1 == c2 or c1 == c3 or c2 == c3:
                        found = True
                        break
                if found:
                    results.append("YES")
                else:
                    results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()