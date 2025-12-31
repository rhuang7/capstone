import sys
import heapq

MOD = 10007

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    # Sort the array
    a.sort()
    
    # Use a min-heap for a and a max-heap for b
    # Since Python only has a min-heap, we can invert the values for max-heap
    a_heap = a
    b_heap = [-x for x in a]
    
    # Heapify
    heapq.heapify(a_heap)
    heapq.heapify(b_heap)
    
    total = 0
    for i in range(n):
        # Get the smallest element from a
        a_val = heapq.heappop(a_heap)
        # Get the largest element from b (inverted)
        b_val = -heapq.heappop(b_heap)
        total += a_val * b_val
        total %= MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()