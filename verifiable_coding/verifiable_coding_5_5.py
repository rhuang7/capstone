import sys
import math
from collections import defaultdict

def solve():
    import sys
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
        
        # Check if there's a possible split
        possible = False
        for l1 in range(1, n):
            l2 = n - l1
            p1 = a[:l1]
            p2 = a[l1:]
            
            # Check if p1 is a permutation of 1..l1
            if len(p1) != len(set(p1)) or any(x > l1 or x < 1 for x in p1):
                continue
            # Check if p2 is a permutation of 1..l2
            if len(p2) != len(set(p2)) or any(x > l2 or x < 1 for x in p2):
                continue
            
            possible = True
            results.append(f"{l1} {l2}")
            break
        
        if not possible:
            results.append("0")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()