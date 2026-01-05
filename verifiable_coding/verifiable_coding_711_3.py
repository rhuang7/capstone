import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        n = len(S)
        total = 0
        
        # Precompute frequency of each character in S
        freq = [0] * 26
        for c in S:
            if c != '?':
                freq[ord(c) - ord('a')] += 1
        
        # For each possible substring
        for i in range(n):
            current = [0] * 26
            for j in range(i, n):
                c = S[j]
                if c != '?':
                    current[ord(c) - ord('a')] += 1
                # Check if this substring is good
                is_good = True
                for k in range(26):
                    # Original count in S
                    original = freq[k]
                    # Count in current substring
                    count = current[k]
                    # Check parity
                    if (original % 2) != (count % 2):
                        is_good = False
                        break
                if is_good:
                    total += 1
        print(total)

if __name__ == '__main__':
    solve()