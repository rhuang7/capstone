import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        cnt = Counter(S)
        freq = list(cnt.values())
        n = len(S)
        freq.sort()
        
        # Find the maximum possible number of distinct characters that can be used
        # such that each occurs exactly k times
        max_k = 0
        for k in range(1, n+1):
            if k * k <= n:
                max_k = k
        
        # Try all possible k from 1 to max_k
        min_ops = n
        for k in range(1, max_k + 1):
            # We need exactly k distinct characters, each appearing exactly k times
            # So total length is k * k
            if k * k > n:
                continue
            # We need to have at least k characters with frequency >= k
            # So count how many characters have frequency >= k
            count = 0
            for f in freq:
                if f >= k:
                    count += 1
            if count >= k:
                # We can use k characters, each appearing exactly k times
                # The number of operations needed is n - k*k
                min_ops = min(min_ops, n - k * k)
        
        print(min_ops)

if __name__ == '__main__':
    solve()