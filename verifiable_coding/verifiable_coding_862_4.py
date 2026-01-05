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
        
        # Create a max-heap
        heap = [-a for a in A]
        heapq.heapify(heap)
        
        total = 0
        
        for _ in range(N):
            # Get the jar with maximum milk
            current = -heapq.heappop(heap)
            
            # If Dhoni can't drink from this jar, Sir Jadeja drinks all
            if current < K or M == 0:
                total += current
                continue
            
            # Dhoni drinks K liters
            remaining = current - K
            total += remaining
            # Put the remaining back into the heap
            heapq.heappush(heap, -remaining)
            M -= 1
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()