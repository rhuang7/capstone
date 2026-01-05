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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        S = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Precompute 2^p for all p in A
        power = [1 << p for p in A]
        
        # Greedy approach: always take the largest possible move
        # Since players play optimally, we simulate the game
        # We'll use a priority queue to always take the largest possible move
        from heapq import heappush, heappop
        # We'll use a max heap (using negative values)
        heap = []
        for p in A:
            heappush(heap, -p)
        
        # Simulate the game
        chef_score = 0
        garry_score = 0
        turn = 0  # 0 for Chef, 1 for Garry
        
        while heap:
            # Get the largest possible p
            p = -heappop(heap)
            # Find the largest x in S that is <= current size of heap
            # We need to find the largest x in S such that x <= len(heap)
            # Since S is given, we can pre-sort it
            # Pre-sort S
            S_sorted = sorted(S)
            x = 0
            for s in S_sorted:
                if s <= len(heap):
                    x = s
                    break
            # If no such x found, the player can't make a move
            if x == 0:
                break
            # Take x elements from the top
            # We need to take the x largest elements
            # Since we have a max heap, we can pop x elements
            # But we need to take the x largest elements, so we pop x times
            # But since we have a max heap, we can just pop x times
            # However, we need to take the x largest elements, which are the first x popped
            # So we pop x times and sum their power
            total = 0
            for _ in range(x):
                if not heap:
                    break
                p = -heappop(heap)
                total += power[p]
            # Add to the current player's score
            if turn % 2 == 0:
                chef_score += total
            else:
                garry_score += total
            turn += 1
        
        if chef_score > garry_score:
            results.append("Chef")
        elif chef_score < garry_score:
            results.append("Garry")
        else:
            results.append("Draw")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()