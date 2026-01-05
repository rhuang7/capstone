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
        
        # The game is equivalent to a Nim game with two piles
        # Each pile represents the number of black cells on each side of the white cell
        # The player to make the last move wins
        # The Grundy number for a pile of size n is n
        # The XOR of the two piles determines the winner
        # If XOR is non-zero, the first player (Aleksa) wins, else the second player (Chef) wins
        
        xor = left ^ right
        if xor != 0:
            print("Aleksa")
        else:
            print("Chef")

if __name__ == '__main__':
    solve()