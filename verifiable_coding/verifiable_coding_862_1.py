import sys
import heapq

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Create a max heap
        heap = []
        for a in A:
            heapq.heappush(heap, -a)
        
        total = 0
        
        for _ in range(N):
            # Get the jar with maximum milk
            max_milk = -heapq.heappop(heap)
            
            # If Dhoni can't drink from this jar or has already drunk M times
            if max_milk < K or M == 0:
                total += max_milk
                continue
            
            # Dhoni drinks K liters
            remaining = max_milk - K
            total += remaining
            # Put the remaining back into the heap
            heapq.heappush(heap, -remaining)
            M -= 1
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()