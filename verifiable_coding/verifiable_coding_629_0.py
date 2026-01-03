import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        M = int(data[idx+3])
        idx += 4
        
        r = list(map(int, data[idx:idx+R]))
        idx += R
        g = list(map(int, data[idx:idx+G]))
        idx += G
        b = list(map(int, data[idx:idx+B]))
        idx += B
        
        # Function to perform magic tricks on a list of potions
        def perform_magic(potions, times):
            for _ in range(times):
                potions.sort(reverse=True)
                potions[0] //= 2
            return max(potions)
        
        # Initial maximum values
        max_r = max(r)
        max_g = max(g)
        max_b = max(b)
        current_max = max(max_r, max_g, max_b)
        
        # Try all possible combinations of magic tricks
        # We can only perform M tricks, so we try all combinations of how many tricks to apply to each color
        # We use a priority queue to find the best way to apply the tricks
        from heapq import heappush, heappop
        
        # Priority queue: (current_max, r_tricks, g_tricks, b_tricks)
        heap = []
        heappush(heap, (current_max, 0, 0, 0))
        
        visited = set()
        while heap:
            current_max, r_tricks, g_tricks, b_tricks = heappop(heap)
            if r_tricks + g_tricks + b_tricks == M:
                results.append(current_max)
                break
            state = (r_tricks, g_tricks, b_tricks)
            if state in visited:
                continue
            visited.add(state)
            
            # Try applying a trick to red
            if r_tricks < M:
                new_r = r.copy()
                for _ in range(r_tricks + 1 - r_tricks):
                    new_r.sort(reverse=True)
                    new_r[0] //= 2
                new_max = max(max(new_r), max_g, max_b)
                heappush(heap, (new_max, r_tricks + 1, g_tricks, b_tricks))
            
            # Try applying a trick to green
            if g_tricks < M:
                new_g = g.copy()
                for _ in range(g_tricks + 1 - g_tricks):
                    new_g.sort(reverse=True)
                    new_g[0] //= 2
                new_max = max(max_r, max(new_g), max_b)
                heappush(heap, (new_max, r_tricks, g_tricks + 1, b_tricks))
            
            # Try applying a trick to blue
            if b_tricks < M:
                new_b = b.copy()
                for _ in range(b_tricks + 1 - b_tricks):
                    new_b.sort(reverse=True)
                    new_b[0] //= 2
                new_max = max(max_r, max_g, max(new_b))
                heappush(heap, (new_max, r_tricks, g_tricks, b_tricks))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()