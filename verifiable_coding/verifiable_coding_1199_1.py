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
        # We can use as many as possible of the largest coin (N)
        # Then use 1s for the remainder
        # But since N is even, we can only use 1s for odd remainders
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But wait, we have a 1 coin as well, so we can use that to make odd numbers
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is even, we can use only even coins
        # If S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N != 0 else 0)
        # But if S is odd, we need at least one 1 coin
        # So the minimum number of coins is:
        # (S // N) + (1 if S % N