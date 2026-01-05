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
        
        # Game is about who can take more "points" by taking x elements
        # Since each move takes exactly x elements, and players alternate
        # We can model this as a game where players take turns taking x elements
        # The player who takes the last element wins
        # But since the score is based on the sum of 2^p, we need to find who can take more points
        
        # We can use Grundy numbers or game theory to determine the winner
        # However, since the game is deterministic and players play optimally, we can simulate the game
        
        # We can simulate the game by considering all possible moves
        # But for efficiency, we can use memoization or dynamic programming
        
        # Since the game is deterministic and the players play optimally, we can simulate the game
        # We can use a recursive approach with memoization to determine the winner
        
        from functools import lru_cache
        
        # We will simulate the game with memoization
        # We will use a memoization cache to store the result for a given state
        # The state is the current stack (represented as a list of values)
        # However, since the stack is large, we need to find a way to represent it efficiently
        
        # Instead of representing the stack as a list, we can represent it as a tuple of the values
        # We will use memoization to store the result for a given state
        
        # We will use a recursive function to simulate the game
        # The function will return the maximum score difference the current player can achieve
        
        @lru_cache(maxsize=None)
        def game(state):
            if not state:
                return 0
            max_diff = -float('inf')
            for x in S:
                if x <= len(state):
                    new_state = state[x:]
                    current_score = sum(1 << p for p in state[:x])
                    diff = current_score - game(new_state)
                    if diff > max_diff:
                        max_diff = diff
            return max_diff
        
        # Initial state is the tuple of the stack
        initial_state = tuple(A)
        score_diff = game(initial_state)
        
        if score_diff > 0:
            results.append("Chef")
        elif score_diff < 0:
            results.append("Garry")
        else:
            results.append("Draw")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()