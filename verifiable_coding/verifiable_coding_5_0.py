import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        valid_lengths = []
        for l1 in range(1, n):
            l2 = n - l1
            p1 = set(a[:l1])
            p2 = set(a[l1:])
            if len(p1) == l1 and len(p2) == l2:
                valid_lengths.append((l1, l2))
        
        results.append(str(len(valid_lengths)))
        for l1, l2 in valid_lengths:
            results.append(f"{l1} {l2}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()