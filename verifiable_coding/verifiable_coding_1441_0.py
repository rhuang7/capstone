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
        
        # Precompute 2^p for all possible p (up to 1e9)
        # But since we need to sum them, we can just compute them on the fly
        # We'll use a greedy approach to determine the optimal moves
        
        # Since the players play optimally, we can model this as a game where each move
        # is to pop x elements from the top of the stack, and the player with higher total
        # score wins. We'll simulate the game with a priority queue of available moves
        
        # We'll use a priority queue to always choose the move that gives the maximum gain
        # in terms of the difference between the current player's score and the opponent's
        # score.
        
        # We'll use a max-heap to simulate the game
        
        # We'll also use a memoization approach to avoid recomputing the same states
        
        # However, for the sake of time and efficiency, we'll use a greedy approach here
        
        # We'll simulate the game step by step
        stack = A
        turn = 0  # 0 for Chef, 1 for Garry
        chef_score = 0
        garry_score = 0
        
        while stack:
            # Get all possible moves (x in S where x <= len(stack))
            possible_moves = [x for x in S if x <= len(stack)]
            if not possible_moves:
                break
            # Choose the move that maximizes the difference between the current player's score
            # and the opponent's score
            max_diff = -1
            best_move = 1
            for x in possible_moves:
                # Simulate the move
                temp_score = 0
                for i in range(x):
                    temp_score += 2 ** stack[-i-1]
                # Calculate the difference if this move is taken
                if turn == 0:
                    diff = temp_score - garry_score
                else:
                    diff = -temp_score + chef_score
                if diff > max_diff:
                    max_diff = diff
                    best_move = x
            # Take the best move
            for i in range(best_move):
                chef_score += 2 ** stack[-i-1]
            stack = stack[best_move:]
            turn = 1 - turn
        
        if chef_score > garry_score:
            results.append("Chef")
        elif chef_score < garry_score:
            results.append("Garry")
        else:
            results.append("Draw")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()