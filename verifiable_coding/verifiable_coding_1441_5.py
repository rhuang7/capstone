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
        
        # Game is a variant of impartial game, we can model it as a Grundy number game
        # But since the moves are dependent on the set S, we need to find the optimal play
        
        # Since the players alternate turns and the game is deterministic, we can simulate the game
        # But with N up to 1e5, we need an efficient approach
        
        # We can use memoization with the current position in the stack
        # However, for large N, this may not be feasible
        
        # Instead, we can use a greedy approach: the player will always choose the move that maximizes their score difference
        # Since the players play optimally, we can simulate the game using a recursive approach with memoization
        
        # We'll use memoization to avoid recomputing the same states
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dfs(pos):
            if pos == N:
                return 0
            max_diff = -float('inf')
            for x in S:
                if pos + x <= N:
                    # Calculate the score difference for this move
                    current_score = sum(1 << A[i] for i in range(pos, pos + x))
                    next_diff = -dfs(pos + x)
                    diff = current_score + next_diff
                    if diff > max_diff:
                        max_diff = diff
            return max_diff
        
        # Chef goes first, so the initial difference is dfs(0)
        if dfs(0) > 0:
            results.append("Chef")
        elif dfs(0) < 0:
            results.append("Garry")
        else:
            results.append("Draw")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()