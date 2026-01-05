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
        # We can use as many as possible of the largest coin (N) and then handle the remainder
        # Since N is even, and we have a 1 coin, we can always make any value
        # The minimum number of coins is:
        # - 1 coin of 1 if S is odd
        # - S // N coins of N if S is even and divisible by N
        # - (S // N) + 1 coins if S is even but not divisible by N
        # - (S // N) + 1 coins if S is odd (we need one 1 coin)
        
        if S % 2 == 1:
            # We need at least one 1 coin
            results.append(1 + (S - 1) // N)
        else:
            # We can use only even coins
            results.append(S // N)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()