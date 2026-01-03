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
        power = [1 << a for a in A]
        
        # Greedy approach: always take the largest possible move
        # Since players play optimally, we simulate the game
        # We'll use a priority queue to always take the largest possible move
        # But since the moves are determined by the set S, we need to simulate the game
        # We'll simulate the game by trying all possible moves in a greedy way
        
        # We'll simulate the game with a stack
        stack = A
        turn = 0  # 0 for Chef, 1 for Garry
        chef_score = 0
        garry_score = 0
        
        while stack:
            # Try all possible moves in S
            # We'll try the moves in descending order to maximize the score
            # Since the set S is given, we can sort it in descending order
            S_sorted = sorted(S, reverse=True)
            move_found = False
            for x in S_sorted:
                if len(stack) >= x:
                    # Pop x elements
                    popped = stack[-x:]
                    stack = stack[:-x]
                    # Add to score
                    if turn == 0:
                        chef_score += sum(1 << p for p in popped)
                    else:
                        garry_score += sum(1 << p for p in popped)
                    move_found = True
                    break
            if not move_found:
                # No move possible, break
                break
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