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
    
    events = []
    for _ in range(N + M):
        events.append(int(data[idx]))
        idx += 1
    
    # We need to track alive people and find the max each time the king comes
    # We can use a max-heap, but since Python only has min-heap, we store negative values
    # Also, we need to track which people are alive
    alive = set()
    max_heap = []
    
    output = []
    
    for event in events:
        if event == -1:
            # King comes, find the max alive
            if max_heap:
                # Pop the max (store as negative)
                max_val = -heapq.heappop(max_heap)
                output.append(str(max_val))
        else:
            # Citizen comes, add to heap and alive set
            heapq.heappush(max_heap, -event)
            alive.add(event)
    
    for line in output:
        print(line)

if __name__ == '__main__':
    solve()