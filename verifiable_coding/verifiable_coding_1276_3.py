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
        or_closure = set()
        or_closure.add(0)
        for num in A:
            new_elements = set()
            for x in or_closure:
                new_elements.add(x | num)
            or_closure.update(new_elements)
        
        # Check if the size of or_closure is a power of 2
        size = len(or_closure)
        if size == (1 << K):
            results.append(0)
            continue
        
        # Find the smallest power of 2 greater than or equal to size
        power = 1
        while power < size:
            power <<= 1
        
        # The number of elements to insert is power - size
        results.append(power - size)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()