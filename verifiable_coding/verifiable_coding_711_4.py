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
        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                if S[j] == '?':
                    cnt[0] += 1
                else:
                    cnt[ord(S[j]) - ord('a')] += 1
                # Check if current substring is good
                is_good = True
                for k in range(26):
                    if (cnt[k] % 2) != (cnt[k] % 2):
                        is_good = False
                        break
                if is_good:
                    res += 1
        print(res)

if __name__ == '__main__':
    solve()