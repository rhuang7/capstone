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
        
        # Max heap to always select the jar with maximum milk
        max_heap = []
        for a in A:
            heapq.heappush(max_heap, -a)
        
        total = 0
        
        for _ in range(N):
            # Get the jar with maximum milk
            current = -heapq.heappop(max_heap)
            
            # If the jar has less than K or Dhoni has already drunk M times from it
            if current < K or M == 0:
                total += current
                continue
            
            # Dhoni drinks K liters
            current -= K
            M -= 1
            
            # Put the remaining milk back into the heap
            heapq.heappush(max_heap, -current)
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()