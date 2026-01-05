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
        # We will simulate the game by always choosing the largest possible x in S that is <= remaining discs
        # We will keep track of the current score for Chef and Garry
        chef_score = 0
        garry_score = 0
        remaining = N
        turn = 0  # 0 for Chef, 1 for Garry
        
        while remaining > 0:
            # Find the largest x in S that is <= remaining
            x = 0
            for s in S:
                if s <= remaining:
                    x = s
                    break
            # If no such x, break (game ends)
            if x == 0:
                break
            # Take x discs
            # Take the top x discs
            taken = power[-x:]
            if turn == 0:
                chef_score += sum(taken)
            else:
                garry_score += sum(taken)
            remaining -= x
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