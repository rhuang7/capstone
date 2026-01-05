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
        
        # Use a max-heap to always pick the jar with the maximum milk
        # To simulate a max-heap, we store negative values
        max_heap = []
        for a in A:
            heapq.heappush(max_heap, -a)
        
        total_sir_jadeja = 0
        
        for _ in range(N):
            # Get the jar with the maximum milk
            current = -heapq.heappop(max_heap)
            
            # Dhoni can drink from this jar up to M times
            # Each time he drinks K liters, but not more than what's in the jar
            # So the number of times Dhoni can drink from this jar is min(M, current // K)
            times_dhoni_can_drink = min(M, current // K)
            
            # Dhoni drinks times_dhoni_can_drink * K liters
            dhoni_drinks = times_dhoni_can_drink * K
            remaining = current - dhoni_drinks
            
            # Sir Jadeja drinks the remaining milk
            total_sir_jadeja = (total_sir_jadeja + remaining) % MOD
            
            # Put the remaining milk back into the heap
            if remaining > 0:
                heapq.heappush(max_heap, -remaining)
        
        results.append(total_sir_jadeja % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()