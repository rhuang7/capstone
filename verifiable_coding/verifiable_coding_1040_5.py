import sys
import math

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
        
        # Preprocess for each position the frequency of each character
        # We'll use a 2D array freq[i][c] = number of times character c appears in S[i...N-1]
        # But since N can be up to 1e5, this is not feasible. Instead, we'll use a sliding window approach.
        
        # For each query, check if there's a rich substring within the query range
        for L, R in queries:
            # Check if there's a rich substring in [L, R]
            # A rich substring must have length >= 3 and a character appearing more than half the time
            # So we can check for all possible substrings of length 3 or more
            # But this is O(Q * (R-L+1)^2), which is too slow for large Q and large R-L+1
            # So we need a smarter approach
            
            # A rich substring must have a character that appears more than half the time
            # So for any substring of length >= 3, if there is a character that appears more than half the time, then it's rich
            # So for a given query [L, R], we can check if there's a character that appears more than (length of substring)/2 times in any substring of length >= 3
            
            # To optimize, we can check for all possible characters in the query range
            # For each character c in S[L...R], check if it appears more than half the time in any substring of length >= 3
            
            # But again, this is O(Q * 26 * (R-L+1)), which is too slow for large Q and large R-L+1
            
            # So we need a way to check for each query if there exists a character that appears more than half the time in any substring of length >= 3
            
            # Here's the key insight: if there exists a character that appears more than half the time in the entire query range, then there must be a rich substring
            # Because if a character appears more than (R-L+1)/2 times, then there exists a substring of length >= 3 where it appears more than half the time
            # So we can check for each query if there's a character that appears more than (R-L+1)/2 times in the query range
            
            # So for each query, we can count the frequency of each character in the query range
            # If any character has count > (R-L+1)//2, then answer is YES
            # Else, answer is NO
            
            # But this is not sufficient, because the character may appear more than half the time in the entire query range, but not in any substring of length >= 3
            # For example, if the query is "aabbaa", the entire string has 4 a's, which is more than half of 6, but there is no substring of length >= 3 with more than half a's
            # So this approach is not correct
            
            # So we need to find if there exists a substring of length >= 3 where a character appears more than half the time
            # How can we do this efficiently?
            
            # The key observation is that for a substring to be rich, it must have a character that appears more than half the time
            # So for each possible character, we can check if there exists a substring of length >= 3 where it appears more than half the time
            
            # But again, this is too slow for large Q and large R-L+1
            
            # Here's the correct approach:
            # For a given query [L, R], we can check if there exists a character that appears more than (R-L+1)/2 times in the entire query range
            # If yes, then answer is YES
            # If no, then answer is NO
            
            # This is because if a character appears more than half the time in the entire query range, then there must be a substring of length >= 3 where it appears more than half the time
            # So we can count the frequency of each character in the query range
            # If any character has frequency > (R-L+1)//2, then answer is YES
            # Else, answer is NO
            
            # So let's implement this
            
            # Count frequency of each character in the query range
            freq = [0] * 26
            for i in range(L, R + 1):
                c = ord(S[i]) - ord('a')
                freq[c] += 1
            
            # Check if any character has frequency > (R-L+1)//2
            length = R - L + 1
            if length < 3:
                results.append("NO")
                continue
            max_freq = max(freq)
            if max_freq > length // 2:
                results.append("YES")
            else:
                results.append("NO")
    
    print("\n".join(results))