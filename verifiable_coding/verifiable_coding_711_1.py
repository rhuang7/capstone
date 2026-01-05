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
        for i in range(n):
            for j in range(i, n):
                substr = S[i:j+1]
                cnt = [0] * 26
                q = 0
                for c in substr:
                    if c == '?':
                        q += 1
                    else:
                        cnt[ord(c) - ord('a')] += 1
                valid = True
                for k in range(26):
                    if (cnt[k] % 2) != (q % 2):
                        valid = False
                        break
                if valid:
                    total += 1
        print(total)

if __name__ == '__main__':
    solve()