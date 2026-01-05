import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    cases = data[1:]
    
    for s in cases:
        n = len(s)
        # For each position in the string, determine the optimal choice to maximize the average wins
        # The optimal choice for each position is the one that beats the bot's choice at that position
        # Rock (R) beats Scissors (S)
        # Scissors (S) beats Paper (P)
        # Paper (P) beats Rock (R)
        # So, for each character in s, we choose the one that beats it
        res = []
        for c in s:
            if c == 'R':
                res.append('P')
            elif c == 'S':
                res.append('P')
            elif c == 'P':
                res.append('S')
        print(''.join(res))
        
if __name__ == '__main__':
    solve()