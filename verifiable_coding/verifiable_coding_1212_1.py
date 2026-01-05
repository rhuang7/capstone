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
        # We try all possible k from 1 to len(freq)
        min_ops = n
        for k in range(1, len(freq) + 1):
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