import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute the OR closure of the array
        unique = set()
        unique.add(0)
        for num in A:
            new_unique = set()
            for x in unique:
                new_unique.add(x | num)
            unique.update(new_unique)
        
        # Check if the size of unique is 2^K
        if len(unique) == (1 << K):
            results.append(0)
            continue
        
        # Compute the minimal number of elements to insert
        # The required size is 2^K
        required = (1 << K)
        current = len(unique)
        # The minimal number of elements to insert is required - current
        results.append(required - current)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()