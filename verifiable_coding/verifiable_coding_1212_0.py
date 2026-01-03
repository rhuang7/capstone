import sys
from collections import Counter

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        cnt = Counter(S)
        freq = list(cnt.values())
        n = len(S)
        freq.sort()
        
        # Find the maximum possible number of distinct characters
        # that can be used in a balanced string
        max_k = 0
        for i in range(len(freq)):
            if freq[i] == 0:
                continue
            if n % (i + 1) == 0:
                max_k = i + 1
        
        # Now try to find the minimum operations
        # by trying all possible k (number of distinct characters)
        min_ops = n  # worst case: all characters are different
        for k in range(1, len(freq)+1):
            if n % k != 0:
                continue
            target = n // k
            ops = 0
            for f in freq:
                if f > target:
                    ops += f - target
            min_ops = min(min_ops, ops)
        
        print(min_ops)

if __name__ == '__main__':
    solve()