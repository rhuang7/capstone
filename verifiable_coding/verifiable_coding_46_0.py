import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:t+1]
    
    for s in cases:
        n = len(s)
        # For each position in the string, determine the best choice to maximize the average wins
        # We need to choose a sequence c such that the sum of wins across all possible starting positions is maximized
        # The optimal choice for each position is the one that beats the bot's choice at that position
        # So, for each position i, choose the move that beats s[i]
        # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
        # So, for each character in s, we choose the move that beats it
        # For 'R', choose 'S'; for 'S', choose 'P'; for 'P', choose 'R'
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