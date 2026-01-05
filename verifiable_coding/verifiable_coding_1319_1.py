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
    
    # We need to track the current alive people and the maximum among them
    # We can use a max-heap, but since Python's heapq is a min-heap, we store negatives
    # Also, we need to track which people are alive
    alive = set()
    max_heap = []
    
    output = []
    
    i = 0
    while i < len(events):
        if events[i] == '-1':
            # King visits, find the richest alive person
            if not max_heap:
                # According to problem statement, this is not possible
                pass
            # Pop the max (which is the negative of the smallest in the heap)
            current_max = -heapq.heappop(max_heap)
            output.append(str(current_max))
            # Remove from alive set
            alive.remove(current_max)
        else:
            # Citizen appears
            wealth = int(events[i])
            # Add to alive set
            alive.add(wealth)
            # Push to heap
            heapq.heappush(max_heap, -wealth)
            i += 1
    
    for line in output:
        print(line)

if __name__ == '__main__':
    solve()