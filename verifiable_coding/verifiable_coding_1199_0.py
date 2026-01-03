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
        # Since N is even, we can use as many N as possible
        coins = remaining // N
        
        # If there is a remainder, we need one more coin
        if remaining % N != 0:
            coins += 1
        
        # Total coins is ones + coins
        results.append(ones + coins)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()