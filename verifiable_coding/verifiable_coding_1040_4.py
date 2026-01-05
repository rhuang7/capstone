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
        
        # Preprocess frequency of each character
        freq = [0] * 26
        for c in S:
            freq[ord(c) - ord('a')] += 1
        
        # For each query, check if there is a rich substring
        for L, R in queries:
            # Check if the entire substring is rich
            max_count = 0
            for c in S[L:R+1]:
                max_count = max(max_count, freq[ord(c) - ord('a')])
            if max_count > (R - L + 1) // 2:
                results.append("YES")
                continue
            
            # Check for any substring of length 3
            found = False
            for i in range(L, R - 1):
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
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()