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
        for __ in range(Q):
            L = int(data[idx]) - 1
            R = int(data[idx+1]) - 1
            idx += 2
            # Check if there is a rich substring in the range [L, R]
            # A rich substring must have length >= 3 and a character that appears more than half the time
            # For any substring of length >= 3, we can check if any character appears more than half the time
            # We can check all possible substrings of length 3, 4, ..., R-L+1
            # However, this is too slow for large N and Q
            # Instead, we can check if there exists a character that appears more than half the time in the entire query range
            # If such a character exists, then there is a rich substring
            # Because if a character appears more than half the time in the entire query range, then there exists a substring of length >= 3 where it appears more than half the time
            # So we can count the frequency of each character in the query range
            freq = [0] * 26
            for i in range(L, R + 1):
                freq[ord(S[i]) - ord('a')] += 1
            found = False
            for i in range(26):
                if freq[i] > (R - L + 1) // 2:
                    found = True
                    break
            results.append("YES" if found else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()