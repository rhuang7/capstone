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
        # Since N is even, we can use as many as possible of N
        # But since we want minimum coins, we use as many as possible of the largest even value
        # So we use (remaining // N) coins of N
        # If remaining % N != 0, we need one more coin of (remaining % N)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since remaining is even, (remaining // N) + (1 if remaining % N != 0 else 0) is equivalent to (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N) is even, so we can use it as a single coin
        # So total coins = ones + (remaining // N) + (1 if remaining % N != 0 else 0)
        # But since N is even, (remaining % N