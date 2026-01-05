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
        
        # Max heap to get the jar with maximum milk
        max_heap = []
        for a in A:
            heapq.heappush(max_heap, -a)
        
        total_sir_jadega = 0
        
        for _ in range(N):
            # Get the jar with maximum milk
            current = -heapq.heappop(max_heap)
            
            # If current jar has less than K or Dhoni has already drunk M times from it
            if current < K or M == 0:
                total_sir_jadega += current
                total_sir_jadega %= MOD
            else:
                # Dhoni drinks K liters
                current -= K
                # Put back the remaining milk
                heapq.heappush(max_heap, -current)
                M -= 1
        
        results.append(total_sir_jadega % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()