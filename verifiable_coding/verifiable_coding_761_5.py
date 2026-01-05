import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        C = list(map(int, data[idx:idx+K]))
        idx += K
        D = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each day, calculate the difference between planned and completed tasks
        diff = [A[i] - B[i] for i in range(N)]
        
        # Sort white buttons in descending order
        C.sort(reverse=True)
        # Sort black buttons in ascending order
        D.sort()
        
        # Use a max heap for white buttons and a min heap for black buttons
        white_heap = C
        black_heap = D
        
        # Greedy approach: use white buttons on days where diff is large and can be reduced
        # Use black buttons on days where diff is small and can be increased
        # We need to track which days have been used
        used = [False] * N
        
        # Use white buttons
        for i in range(N):
            if not used[i] and diff[i] > 0:
                # Try to use a white button on this day
                if white_heap:
                    x = white_heap[0]
                    if diff[i] >= x:
                        diff[i] -= x
                        heapq.heappop(white_heap)
                        used[i] = True
        
        # Use black buttons
        for i in range(N):
            if not used[i] and diff[i] > 0:
                # Try to use a black button on this day
                if black_heap:
                    x = black_heap[0]
                    if B[i] + x <= A[i]:
                        B[i] += x
                        heapq.heappop(black_heap)
                        used[i] = True
        
        # Calculate the total uncompleted tasks
        total = sum(A[i] - B[i] for i in range(N))
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()