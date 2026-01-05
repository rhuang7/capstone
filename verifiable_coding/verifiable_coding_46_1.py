import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:]
    
    for s in cases:
        n = len(s)
        # For each position in the string, determine the best choice to maximize the average
        # We need to choose a strategy that maximizes the total wins across all possible starting positions
        # The optimal strategy is to choose the move that beats the bot's move at that position
        # So, for each character in s, we choose the move that beats it
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