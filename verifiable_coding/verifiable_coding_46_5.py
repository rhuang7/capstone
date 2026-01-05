import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:t+1]
    
    for s in cases:
        n = len(s)
        # For each position, determine the best choice to maximize the average
        # We need to choose a sequence c such that the sum of wins over all possible starting positions is maximized
        # The optimal strategy is to choose the move that beats the bot's move at that position
        # So for each position i, choose the move that beats s[i]
        # For example, if s[i] is 'R', choose 'S' (beats Rock)
        # If s[i] is 'S', choose 'P' (beats Scissors)
        # If s[i] is 'P', choose 'R' (beats Paper)
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