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
        odd_coins = S // 2
        
        # If S is odd, we need at least one 1 coin
        if S % 2 == 1:
            odd_coins += 1
        
        # The remaining amount after using 1 coin (if needed) is even
        remaining = S - (1 if S % 2 == 1 else 0)
        
        # Number of coins needed for the even part
        even_coins = remaining // N
        
        # Total coins
        total_coins = odd_coins + even_coins
        
        results.append(str(total_coins))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()