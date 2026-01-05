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
    
    # We need to track the current alive citizens and the maximum wealth
    # We can use a max-heap to track the current maximum
    # However, since we need to remove elements when the king visits, we need a way to track which elements are still alive
    # We can use a min-heap to track the current maximum, but we need to handle the alive status
    # We'll use a set to track the alive citizens
    
    alive = set()
    max_heap = []
    
    output = []
    
    for event in events:
        if event == '-1':
            # King visits, need to behead the richest alive
            if not alive:
                # According to the problem statement, this is not possible
                pass
            # Find the maximum in the alive set
            # We can use a max-heap, but since we need to remove elements, we can use a min-heap with negative values
            # So we need to maintain a max-heap of the alive citizens
            # But since we can't efficiently remove elements from a heap, we can use a lazy removal approach
            # So we keep a max-heap, and a set of alive elements
            # When the king visits, we pop the max element from the heap, but only if it's still alive
            # If it's not alive, we continue popping until we find one that is alive
            while max_heap:
                current = -max_heap[0]
                if current in alive:
                    output.append(str(current))
                    alive.remove(current)
                    heapq.heappop(max_heap)
                    break
        else:
            # Citizen appears
            wealth = int(event)
            alive.add(wealth)
            heapq.heappush(max_heap, -wealth)
    
    for line in output:
        print(line)

if __name__ == '__main__':
    solve()