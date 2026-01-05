import sys
import itertools

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+N]))
        idx += N
        meal_sets = []
        for _ in range(M):
            Pi = int(data[idx])
            Qi = int(data[idx+1])
            idx += 2
            A = list(map(int, data[idx:idx+Qi]))
            idx += Qi
            meal_sets.append((Pi, A))
        
        # Preprocess meals to be 0-based
        meals = [0] * N
        for i in range(N):
            meals[i] = i
        
        # For each meal set, create a bitmask of the meals it contains
        set_masks = []
        for Pi, A in meal_sets:
            mask = 0
            for a in A:
                mask |= 1 << (a - 1)
            set_masks.append((Pi, mask))
        
        # We need to have all N meals, so the target mask is (1 << N) - 1
        target_mask = (1 << N) - 1
        
        # Use dynamic programming to find the minimum cost to achieve each mask
        dp = [float('inf')] * (1 << N)
        dp[0] = 0
        
        for mask in range(1 << N):
            if dp[mask] == float('inf'):
                continue
            # Try adding each meal set
            for Pi, set_mask in set_masks:
                new_mask = mask | set_mask
                if new_mask == target_mask:
                    if dp[mask] + Pi < dp[new_mask]:
                        dp[new_mask] = dp[mask] + Pi
                else:
                    if dp[mask] + Pi < dp[new_mask]:
                        dp[new_mask] = dp[mask] + Pi
        
        # Also consider buying individual meals
        for i in range(N):
            if dp[1 << i] > C[i]:
                dp[1 << i] = C[i]
        
        # Find the minimum cost to get all meals
        results.append(str(dp[target_mask]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()