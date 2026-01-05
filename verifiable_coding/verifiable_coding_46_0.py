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
        # We need to choose a choice for each round such that the total wins across all starting positions is maximized
        # For each position i in the string, we want to choose a choice that beats the bot's choice at that position
        # So, for each character in s, we choose the best counter
        res = []
        for c in s:
            if c == 'R':
                res.append('P')
            elif c == 'S':
                res.append('R')
            else:
                res.append('S')
        print(''.join(res))
        
if __name__ == '__main__':
    solve()