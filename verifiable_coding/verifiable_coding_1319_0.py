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
    
    for event in events:
        if event == '-1':
            if heap:
                result.append(str(heapq.heappop(heap)))
        else:
            wealth = int(event)
            heapq.heappush(heap, -wealth)
    
    for line in result:
        print(line)

if __name__ == '__main__':
    solve()