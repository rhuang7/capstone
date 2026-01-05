import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        S = int(data[index])
        N = int(data[index + 1])
        index += 2
        
        # Number of coins needed for the odd part
        odd_part = S % 2
        coins = 0
        
        # If S is odd, we need at least one 1 coin
        if odd_part == 1:
            coins += 1
            S -= 1
        
        # Now S is even, use as many N coins as possible
        coins += S // N
        
        results.append(str(coins))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()