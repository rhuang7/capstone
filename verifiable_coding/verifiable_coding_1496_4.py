import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    def get_node_number(s):
        level = 1
        pos = 0
        for c in s:
            if c == 'l':
                pos = 2 * pos
            else:
                pos = 2 * pos + 1
            level += 1
        
        # Calculate the number based on level and position
        if level % 2 == 1:
            # Odd level: odd numbering
            num = 1 + 2 * (pos)
        else:
            # Even level: even numbering
            num = 2 + 2 * (pos)
        
        return num
    
    for s in cases:
        print(get_node_number(s))
        
if __name__ == '__main__':
    solve()