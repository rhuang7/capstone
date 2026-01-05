import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        w_pos = s.index('W')
        left = s[:w_pos].count('B')
        right = s[w_pos+1:].count('B')
        
        # The game is played on the left and right of the white cell
        # Each player can take any number of black cells from one side only
        # This is equivalent to a Nim game with two piles: left and right
        # The player to make the last move wins
        
        # The XOR of the two piles determines the winner
        # If XOR is non-zero, the first player (Aleksa) wins, else Chef wins
        if (left ^ right) != 0:
            print("Aleksa")
        else:
            print("Chef")

if __name__ == '__main__':
    solve()