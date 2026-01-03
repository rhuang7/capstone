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
        # Each player can take any number of black cells from one side
        # This is a variant of the Nim game with two piles
        # The player who cannot make a move loses
        # The winner is determined by the XOR of the two piles
        # If XOR is non-zero, first player (Aleksa) wins, else second player (Chef) wins
        
        xor = left ^ right
        if xor != 0:
            print("Aleksa")
        else:
            print("Chef")

if __name__ == '__main__':
    solve()