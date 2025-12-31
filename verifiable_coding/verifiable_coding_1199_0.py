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
        
        # Number of coins needed for S
        # If S is odd, we need at least one 1 coin
        # Then, the rest can be covered by even coins
        coins = 0
        
        if S % 2 == 1:
            coins += 1
            S -= 1
        
        # Now S is even, we can use the largest even coin (N) as much as possible
        coins += S // N
        
        results.append(str(coins))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()