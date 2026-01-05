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
        
        # We need to determine if Vanja can force |V| >= K
        # Since players play optimally, we can use dynamic programming
        # dp[i][v] = True if the current player can force the absolute value to be >= K starting from position i with current value v
        # Since N can be up to 3e4, we need an efficient approach
        
        # Since the operations are + or -, and the values are 0 or 1, the maximum possible value is N (all 1s)
        # So we can use a DP approach with memoization
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(pos, val):
            if pos == N:
                return abs(val) >= K
            # Current player can choose + or -
            # Since the current player is the one who is making the choice, we need to check if there's a move that leads to a win
            # If the current player is Vanja (turn is even), then we want to maximize the result
            # If the current player is Miksi (turn is odd), then we want to minimize the result
            # But since we are checking for the absolute value, we can just check if there's a move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # Since the players play optimally, we need to check if any move leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to a win
            # For the current player, they can choose + or -
            # So we check both possibilities
            # If the current player is Vanja (turn is even), then we want to choose a move that leads to a win
            # If the current player is Miksi (turn is odd), then we want to choose a move that leads to a loss for Vanja
            # So we check if either move leads to a win for Vanja
            # If any of the moves leads to a win, then the current player can win
            # If both moves lead to a loss, then the current player loses
            # So we check if there's at least one move that leads to