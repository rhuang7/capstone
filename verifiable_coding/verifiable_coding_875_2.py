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
        N = int(data[idx])
        Z1 = int(data[idx+1])
        Z2 = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if either Z1 or Z2 is 0
        # If so, the first player can choose that value and win immediately
        if Z1 == 0 or Z2 == 0:
            results.append(1)
            continue
        
        # Check if any element in A can reach Z1 or Z2 in one move
        can_win = False
        for a in A:
            if abs(a) == Z1 or abs(a) == Z2:
                can_win = True
                break
        
        if can_win:
            results.append(1)
            continue
        
        # Check if any element in A can reach Z1 or Z2 in two moves
        # For two moves, the possible values are ±a ±b
        # But since the game can end in 10^10 moves, we need to check if it's possible to reach Z1 or Z2 in any number of moves
        # However, since the players play optimally, we need to check if the first player can force a win in one move, and if not, check if the second player can force a win in one move
        
        # Check if the second player can win in one move
        # For the second player to win, the first player must not be able to win in one move, and the second player must be able to reach Z1 or Z2 in one move
        # So, check if there exists a value in A that can reach Z1 or Z2 when added or subtracted to any value that the first player can't reach in one move
        
        # But since the first player can choose any value in A and add or subtract it, the second player can't force a win unless the first player can't reach Z1 or Z2 in one move, and the second player can reach it in one move
        # So, check if the first player can't reach Z1 or Z2 in one move, and the second player can reach it in one move
        
        # So, check if the first player can't reach Z1 or Z2 in one move, and the second player can reach it in one move
        first_can_win = False
        for a in A:
            if abs(a) == Z1 or abs(a) == Z2:
                first_can_win = True
                break
        
        if not first_can_win:
            second_can_win = False
            for a in A:
                if abs(a) == Z1 or abs(a) == Z2:
                    second_can_win = True
                    break
            if second_can_win:
                results.append(2)
                continue
        
        # If neither player can win in one move, then the game is a tie
        results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()