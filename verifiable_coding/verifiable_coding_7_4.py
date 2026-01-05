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
        
        # Use a priority queue (min-heap) to select the cheapest way to get each voter
        import heapq
        heap = []
        total = 0
        
        for m, p in voters:
            # If we have enough voters already, we can get this voter for free
            if len(heap) >= m:
                continue
            # Otherwise, we need to pay for this voter
            heapq.heappush(heap, p)
            total += p
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()