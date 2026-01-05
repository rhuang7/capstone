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
    
    # Use a min-heap for the laziness levels
    heapq.heapify(a)
    
    total = 0
    # Use a max-heap for the difficulty levels
    # To simulate a max-heap, we insert negative values
    max_heap = [-x for x in a]
    heapq.heapify(max_heap)
    
    for _ in range(n):
        # Get the smallest laziness
        laziness = heapq.heappop(a)
        # Get the largest difficulty
        difficulty = -heapq.heappop(max_heap)
        total += laziness * difficulty
        total %= MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()