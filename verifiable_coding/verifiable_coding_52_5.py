import sys
import heapq

MOD = 10007

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    # Sort the list
    a.sort()
    
    # Use a min-heap for the a values
    heapq.heapify(a)
    
    total = 0
    # Use a max-heap for the a values (simulated with negative values)
    max_heap = [-x for x in a]
    heapq.heapify(max_heap)
    
    for _ in range(n):
        # Pop the smallest from the min-heap
        min_val = heapq.heappop(a)
        # Pop the largest from the max-heap
        max_val = -heapq.heappop(max_heap)
        # Calculate the product
        product = min_val * max_val
        total += product
        total %= MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()