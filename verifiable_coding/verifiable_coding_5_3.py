import sys
import bisect
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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        # Check if all numbers from 1 to n are present
        valid = True
        for i in range(1, n+1):
            if freq[i] != 1:
                valid = False
                break
        if not valid:
            results.append("0")
            continue
        
        # Find possible l1
        possible_l1 = []
        for l1 in range(1, n):
            # Check if the first l1 elements form a permutation
            s1 = set(a[:l1])
            if len(s1) != l1:
                continue
            # Check if the remaining elements form a permutation
            s2 = set(a[l1:])
            if len(s2) != (n - l1):
                continue
            possible_l1.append(l1)
        
        results.append(str(len(possible_l1)))
        for l1 in possible_l1:
            results.append(f"{l1} {n - l1}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()