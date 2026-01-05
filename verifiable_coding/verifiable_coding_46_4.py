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
        # We need to choose a choice for each round such that the sum of wins across all possible starting positions is maximized
        # The optimal choice for each round is the one that beats the bot's choice in that round
        # So, for each character in the string, we choose the move that beats it
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