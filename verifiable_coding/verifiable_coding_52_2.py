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
    
    # Create a max-heap for the second half
    b = a[n//2:]
    for i in range(len(b)):
        b[i] = -b[i]
    heapq.heapify(b)
    
    total = 0
    for i in range(n//2):
        total += a[i] * (-b[i])
        total %= MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()