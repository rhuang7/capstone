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
    heapq.heapify(a)
    
    # Create a max-heap for the second part
    b = [-x for x in a]
    heapq.heapify(b)
    
    total = 0
    for i in range(n):
        # Take the smallest from a and the largest from b
        smallest = heapq.heappop(a)
        largest = -heapq.heappop(b)
        total += smallest * largest
        total %= MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()