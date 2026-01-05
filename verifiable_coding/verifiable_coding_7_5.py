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
        
        # Use a priority queue to track the minimum cost to get a certain number of voters
        import heapq
        heap = []
        total = 0
        count = 0
        
        for m, p in voters:
            # If we have enough voters already, we can skip this one
            if count >= n - m:
                continue
            # Add this voter to the heap
            heapq.heappush(heap, p)
            # If we have more than n voters, we need to remove the most expensive one
            if len(heap) > n:
                heapq.heappop(heap)
            # Update the total cost
            total += p
            count += 1
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()