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
        
        # Use a max-heap to always select the jar with maximum milk
        # Since Python only has a min-heap, we store negative values
        heap = []
        for a in A:
            heapq.heappush(heap, -a)
        
        total_sir_jadeja = 0
        
        for _ in range(N):
            # Get the jar with maximum milk
            max_milk = -heapq.heappop(heap)
            
            # Dhoni can drink from this jar up to M times
            # Each time he drinks K liters, but not more than available
            # If he drinks from it M times, then the remaining milk is drunk by Sir Jadeja
            # Otherwise, after drinking, the jar is put back with remaining milk
            
            # How many times can Dhoni drink from this jar?
            times = min(M, max_milk // K)
            
            # If times is 0, then Sir Jadeja drinks all
            if times == 0:
                total_sir_jadeja = (total_sir_jadeja + max_milk) % MOD
            else:
                # Dhoni drinks times * K liters
                # Remaining milk is max_milk - times * K
                remaining = max_milk - times * K
                # Put the remaining back into the heap
                heapq.heappush(heap, -remaining)
                # Add the milk that Sir Jadeja will drink from this jar
                total_sir_jadeja = (total_sir_jadeja + remaining) % MOD
        
        results.append(total_sir_jadeja)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()