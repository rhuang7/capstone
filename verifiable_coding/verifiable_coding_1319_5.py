import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    events = data[2:]
    
    citizens = []
    heap = []
    result = []
    
    for i, event in enumerate(events):
        if event == '-1':
            # King visits, find the richest alive citizen
            if heap:
                richest = heapq.heappop(heap)
                result.append(richest)
        else:
            # Citizen appears, add to heap
            wealth = int(event)
            heapq.heappush(heap, -wealth)
    
    for line in result:
        print(-line)

if __name__ == '__main__':
    solve()