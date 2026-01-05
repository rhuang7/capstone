import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:t+1]
    
    for s in cases:
        n = len(s)
        # For each position in the string, determine the best choice to maximize the average
        # We will choose the move that beats the bot's move in that position
        # If the bot's move is R, we choose S (Scissors)
        # If the bot's move is S, we choose P (Paper)
        # If the bot's move is P, we choose R (Rock)
        res = []
        for c in s:
            if c == 'R':
                res.append('S')
            elif c == 'S':
                res.append('P')
            else:
                res.append('R')
        print(''.join(res))
        
if __name__ == '__main__':
    solve()