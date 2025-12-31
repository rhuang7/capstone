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
        # Each move reduces one pile (left or right) by any positive amount
        # The winner is determined by the XOR of the two piles
        # If XOR is non-zero, Aleksa (first player) wins, else Chef wins
        
        if left == 0 and right == 0:
            print("Chef")
        else:
            if (left ^ right) != 0:
                print("Aleksa")
            else:
                print("Chef")

if __name__ == '__main__':
    solve()