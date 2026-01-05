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
        prefix = [ [0]*26 for _ in range(N+1) ]
        for i in range(N):
            for j in range(26):
                prefix[i+1][j] = prefix[i][j]
            c = ord(S[i]) - ord('a')
            prefix[i+1][c] += 1
        
        # Process each query
        for L, R in queries:
            # Check if there is a rich substring in the range [L, R]
            # A rich substring must have length >= 3 and a character appearing more than half the time
            # So check all possible substrings of length 3, 4, ..., up to R-L+1
            # But since checking all is too slow, we can optimize by checking for each character in the range
            # If any character appears more than half the length of the substring, then it's rich
            # So for each character in the range, check if it appears more than half of the length of any possible substring
            # But this is still too slow, so we can optimize by checking for each character in the range
            # If any character appears more than half of the length of the entire range, then there exists a rich substring
            # So check if any character appears more than (R-L+1)//2 times in the range
            # If yes, then there exists a rich substring of length >= 3
            # So check if any character appears more than (R-L+1)//2 times in the range
            # If yes, then answer is YES, else NO
            # But this is not sufficient, because even if a character appears more than half of the entire range, it may not appear more than half of a substring of length >=3
            # So we need to check for each possible substring of length >=3
            # But this is too slow for large N and Q
            # So we can use the following observation:
            # If there exists a character that appears more than (R-L+1)//2 times in the entire range, then there exists a rich substring
            # Because that character appears more than half of the entire range, so there exists a substring of length >=3 where it appears more than half the time
            # So we can check for each query if any character appears more than (R-L+1)//2 times in the range
            # If yes, then answer is YES, else NO
            # So for each query, we can check for each character in the range
            # How to do this efficiently?
            # For each query, we can count the frequency of each character in the range [L, R]
            # Then check if any character has frequency > (R-L+1)//2
            # If yes, then answer is YES, else NO
            # This is O(Q * 26 * logN) time, which is acceptable for N and Q up to 1e5
            # So let's proceed with this approach
            # Count frequency of each character in [L, R]
            freq = [0]*26
            for i in range(L, R+1):
                c = ord(S[i]) - ord('a')
                freq[c] += 1
            # Check if any character has frequency > (R-L+1)//2
            length = R - L + 1
            if length < 3:
                results.append("NO")
                continue
            half = length // 2
            for i in range(26):
                if freq[i] > half:
                    results.append("YES")
                    break
            else:
                results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()