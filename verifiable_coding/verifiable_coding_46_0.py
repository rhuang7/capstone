import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:]
    
    for s in cases:
        n = len(s)
        # For each position, determine the best choice to maximize the average
        # We need to choose c_i such that the sum of wins over all possible pos is maximized
        # For each position i, we want to choose c_i to maximize the number of wins when the bot starts at pos
        # So for each i, we choose c_i to beat the bot's choice at i, or draw if it's the same
        # But since we want to maximize the average, we need to choose c_i such that for as many pos as possible, the choice at i wins
        # The optimal strategy is to choose c_i to beat the bot's choice at i
        # Because if the bot starts at pos, the bot's choice is s[pos], and we want to choose c_i to beat it
        # So for each i, choose c_i to beat s[i]
        # The optimal choice for each position is to choose the move that beats the bot's move at that position
        # For example, if s[i] is 'R', choose 'P' (Paper beats Rock)
        # If s[i] is 'S', choose 'R' (Rock beats Scissors)
        # If s[i] is 'P', choose 'S' (Scissors beats Paper)
        res = []
        for ch in s:
            if ch == 'R':
                res.append('P')
            elif ch == 'S':
                res.append('R')
            else:
                res.append('S')
        print(''.join(res))
        
if __name__ == '__main__':
    solve()