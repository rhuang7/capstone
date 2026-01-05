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
        res = 0
        
        # Precompute the count of each character in S
        cnt = [0] * 26
        for c in S:
            if c != '?':
                cnt[ord(c) - ord('a')] += 1
        
        # For each substring, check if it's good
        for i in range(n):
            curr_cnt = [0] * 26
            for j in range(i, n):
                c = S[j]
                if c != '?':
                    curr_cnt[ord(c) - ord('a')] += 1
                # Check if this substring is good
                is_good = True
                for k in range(26):
                    # Original count in S
                    orig = cnt[k]
                    # Count in substring
                    sub = curr_cnt[k]
                    # Check parity
                    if (orig % 2) != (sub % 2):
                        is_good = False
                        break
                if is_good:
                    res += 1
        print(res)

if __name__ == '__main__':
    solve()