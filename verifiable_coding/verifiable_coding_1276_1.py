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
        OR_closure = set()
        queue = A
        while queue:
            num = queue.pop()
            OR_closure.add(num)
            for val in A:
                if (num | val) not in OR_closure:
                    queue.append(num | val)
        
        # Check if the size of OR closure is 2^K
        if len(OR_closure) == (1 << K):
            results.append(0)
            continue
        
        # Compute the minimal number of elements to insert
        # The OR closure must be a subset of {0, 1, ..., 2^K - 1}
        # We need to make sure that the OR closure is exactly {0, 1, ..., 2^K - 1}
        # So we need to find the missing elements in the OR closure
        missing = []
        for x in range(1 << K):
            if x not in OR_closure:
                missing.append(x)
        
        # The minimal number of elements to insert is the number of missing elements
        results.append(len(missing))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()