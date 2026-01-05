import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2
    
    events = data[idx:]
    
    # We need to track the current alive citizens and the maximum among them
    # We'll use a max-heap, but Python's heapq is a min-heap, so we store negatives
    # Also, we need to track the current maximum, which is the top of the heap
    # We'll also need to track which citizens are alive
    
    # We'll use a set to track alive citizens
    alive = set()
    # We'll use a max-heap (simulated with min-heap of negatives)
    heap = []
    
    # We'll also track the current maximum, which is the top of the heap
    # But since we need to find the maximum at each king's visit, we'll just use the heap
    
    output = []
    
    for event in events:
        if event == '-1':
            # King visits, we need to behead the richest alive
            # The richest is the top of the heap
            if heap:
                # Pop the max (which is the negative of the min in the heap)
                max_wealth = -heapq.heappop(heap)
                output.append(str(max_wealth))
        else:
            # Citizen appears, add to alive and to the heap
            wealth = int(event)
            alive.add(wealth)
            heapq.heappush(heap, -wealth)
    
    for line in output:
        print(line)

if __name__ == '__main__':
    solve()