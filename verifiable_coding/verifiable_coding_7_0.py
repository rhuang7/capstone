import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        voters = []
        for _ in range(n):
            m_i = int(data[idx])
            p_i = int(data[idx + 1])
            idx += 2
            voters.append((m_i, p_i))
        
        # Sort voters by m_i in descending order
        voters.sort(reverse=True, key=lambda x: x[0])
        
        # Use a priority queue (min-heap) to track the cost of each group
        import heapq
        heap = []
        
        for m, p in voters:
            # If the current group has more members than the heap's top, we need to merge
            while heap and heap[0][0] < m:
                # Pop the top element and merge
                prev_m, prev_p = heapq.heappop(heap)
                m += prev_m
                p += prev_p
            heapq.heappush(heap, (m, p))
        
        # The total cost is the sum of the p values in the heap
        total = sum(p for (m, p) in heap)
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()