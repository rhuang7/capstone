import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    events = data[2:]
    
    people = []
    max_heap = []
    result = []
    
    for event in events:
        if event == '-1':
            # King visits, find the richest alive person
            if max_heap:
                richest = -heapq.heappop(max_heap)
                result.append(str(richest))
        else:
            # Citizen arrives
            wealth = int(event)
            heapq.heappush(max_heap, -wealth)
    
    for line in result:
        print(line)

if __name__ == '__main__':
    solve()