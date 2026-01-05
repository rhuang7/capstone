import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    events = data[idx:]
    
    # We need to track the current alive citizens and the maximum among them
    # We use a max-heap, but Python's heapq is a min-heap, so we store negatives
    # Also, we need to track the current maximum, so we can efficiently find it
    # We use a separate variable to track the current maximum
    # We also need to track which citizens are alive
    
    alive = set()
    max_heap = []
    current_max = -1
    
    output = []
    
    for event in events:
        if event == '-1':
            # King visits, need to behead the current max
            if current_max == -1:
                # According to problem statement, this is not possible
                pass
            output.append(str(current_max))
            # Remove the current max from alive and from the heap
            alive.remove(current_max)
            # Rebuild the max_heap and current_max
            max_heap = []
            current_max = -1
            for wealth in alive:
                heapq.heappush(max_heap, -wealth)
            if max_heap:
                current_max = -max_heap[0]
        else:
            wealth = int(event)
            alive.add(wealth)
            # Update the max_heap and current_max
            heapq.heappush(max_heap, -wealth)
            if wealth > current_max:
                current_max = wealth
    
    for line in output:
        print(line)

if __name__ == '__main__':
    solve()