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
        # We'll use a 2D array: freq[i][c] = number of occurrences of character c in S[i...N-1]
        # Since N can be up to 1e5, we need an efficient way
        # We'll use a list of dictionaries
        # But for speed, we'll use a list of arrays (for 26 letters)
        # Precompute prefix sums for each character
        # For each character c in 'a' to 'z', compute prefix_sum[c][i] = number of c in S[0..i-1]
        # Then for any substring [L, R], the count of c is prefix_sum[c][R+1] - prefix_sum[c][L]
        
        # Initialize prefix sums for each character
        prefix = [ [0]*(N+1) for _ in range(26) ]
        for i in range(N):
            for c in range(26):
                prefix[c][i+1] = prefix[c][i]
            current_char = ord(S[i]) - ord('a')
            prefix[current_char][i+1] += 1
        
        # For each query, check if there exists a substring of length >=3 that is rich
        # A rich substring must have a character that appears more than half the length of the substring
        # So for a substring of length L, the character must appear at least (L//2 + 1) times
        # We can check for all possible substrings of length >=3 in the query range [L, R]
        # But that would be O((R-L+1)^2) per query, which is too slow for large N and Q
        
        # So we need a smarter way
        # For a substring to be rich, it must have a character that appears more than half of its length
        # This is equivalent to having a character that appears at least (length + 1) // 2 times
        # So for a substring of length L, the character must appear at least (L + 1) // 2 times
        
        # For a given query [L, R], we can check for all possible characters c in 'a' to 'z'
        # and for all possible lengths l from 3 to (R - L + 1)
        # and see if there exists a substring of length l in [L, R] where c appears at least (l + 1) // 2 times
        
        # But even this is O(26 * (R-L+1)) per query, which is too slow for large Q
        
        # So we need to find a way to check for each query if there exists any character c that appears more than half of some substring of length >=3 in [L, R]
        
        # Let's think differently: for a substring to be rich, it must have a character that appears more than half of its length
        # So for any character c, if it appears at least k times in some substring of length >=2k-1, then that substring is rich
        # So for each query, we can check for each character c if it appears at least k times in some substring of length >=2k-1
        
        # But again, this is not efficient
        
        # Let's think of the following: for any substring of length >=3, if there is a character that appears more than half of the length, then it is rich
        # So for a query [L, R], if there exists a character c that appears at least (length + 1) // 2 times in some substring of length >=3 within [L, R], then answer is YES
        
        # So for each query, we can check for each character c in 'a' to 'z':
        #   For each possible length l from 3 to (R - L + 1):
        #       check if there exists a substring of length l in [L, R] where c appears at least (l + 1) // 2 times
        
        # But this is O(26 * (R-L+1)) per query, which is too slow for large Q
        
        # So we need to find a way to check for each query if there exists a character that appears more than half of some substring of length >=3 in [L, R]
        
        # Let's think of the following: for a query [L, R], if there is a character c that appears at least (R - L + 1 + 1) // 2 times in the entire substring [L, R], then there exists a rich substring
        # Because if a character appears more than half of the entire substring, then the entire substring is rich
        # So for each query, check if any character appears more than half of the length of the substring [L, R]
        
        # This is O(26) per query, which is acceptable
        
        # So the solution is:
        # For each query [L, R], check if any character appears more than (R - L + 1) // 2 times in the substring [L, R]
        # If yes, then answer is YES, else NO
        
        # So the problem reduces to, for each query, check if any character appears more than half of the length of the substring [L, R]
        
        # So how to do this efficiently?
        # We can use the prefix sums for each character
        
        for L, R in queries:
            length = R - L + 1
            if length < 3:
                results.append("NO")
                continue
            max_count = 0
            for c in range(26):
                count = prefix[c][R+1] - prefix[c][L]
                if count > max_count:
                    max_count = count
            if max_count > (length) // 2:
                results.append("YES")
            else:
                results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()