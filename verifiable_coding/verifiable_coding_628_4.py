import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i]
        w_pos = S.index('W')
        left = 0
        right = 0
        
        for c in S:
            if c == 'B':
                if S.index('W') > S.index(c):
                    right += 1
                else:
                    left += 1
        
        # The game is similar to Nim game with two piles
        # The player can take from one pile only
        # The Grundy number for a pile of size n is n
        # The XOR of the two piles determines the winner
        # If XOR is non-zero, first player wins, else second player wins
        
        # But since players can only take from one side, it's equivalent to a single pile
        # The number of black cells on one side is the pile size
        # The player can take any number of cells from that pile
        # So the game is equivalent to a single pile of size n
        # If n is zero, first player loses
        # If n is non-zero, first player wins
        
        if left == 0 and right == 0:
            results.append("Chef")
        else:
            if left == 0 or right == 0:
                results.append("Aleksa")
            else:
                if left == right:
                    results.append("Aleksa")
                else:
                    results.append("Aleksa")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()