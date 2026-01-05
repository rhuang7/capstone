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
        
        # Number of 1 coins needed
        ones = S % 2
        
        # Remaining amount after using 1 coins
        remaining = S - ones
        
        # Number of even coins needed
        # Maximum even value is N, so we use as many as possible
        # Each even coin is of value N, so coins = remaining // N
        coins = remaining // N
        
        # Total coins is ones + coins
        total_coins = ones + coins
        
        results.append(str(total_coins))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()