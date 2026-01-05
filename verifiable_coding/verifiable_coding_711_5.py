import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    def count_letters(s):
        cnt = [0] * 26
        for c in s:
            if c != '?':
                cnt[ord(c) - ord('a')] += 1
        return cnt
    
    def is_good(sub, original_cnt):
        cnt = count_letters(sub)
        for i in range(26):
            if (original_cnt[i] % 2) != (cnt[i] % 2):
                return False
        return True
    
    def solve_case(s):
        n = len(s)
        original_cnt = count_letters(s)
        total = 0
        
        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                c = s[j]
                if c != '?':
                    cnt[ord(c) - ord('a')] += 1
                # Check if current substring is good
                is_good_sub = True
                for k in range(26):
                    if (original_cnt[k] % 2) != (cnt[k] % 2):
                        is_good_sub = False
                        break
                if is_good_sub:
                    total += 1
        return total
    
    for s in cases:
        print(solve_case(s))

if __name__ == '__main__':
    solve()