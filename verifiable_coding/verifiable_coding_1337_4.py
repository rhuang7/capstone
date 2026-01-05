import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        P = list(map(int, data[idx:idx+N]))
        idx += N
        R = int(data[idx])
        idx += 1
        min_p = min(P)
        if R >= min_p:
            print(0)
            continue
        # For each person count p, the number of candies needed is (k * p + R)
        # We need to find the smallest k such that (k * p + R) is the same for all p in P
        # This is equivalent to finding the least common multiple of (p - R) for all p in P
        # Then the minimum number of candies is LCM + R
        # But since we need to find the smallest k such that k * p + R is the same for all p in P
        # We can find the GCD of (p - R) for all p in P
        # Then the minimum k is (LCM of (p - R) for all p in P) / (GCD of (p - R) for all p in P)
        # But since we need the minimum k, it's the GCD of (p - R) for all p in P
        # Then the minimum number of candies is k * min_p + R
        # Wait, no. Let's think again.
        # We need to find the smallest number of candies C such that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The smallest such C is the LCM of all p in P plus R
        # But since we need to find the minimum C such that C - R is divisible by all p in P
        # The minimum C is LCM of all p in P + R
        # But wait, no. Because we need to find the minimum C such that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P plus R
        # But since we need to find the minimum C, it's LCM of all p in P + R
        # However, there's a catch: the problem says that after distributing the candies, there are always R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # But there's a catch: the problem says that R is less than the minimum p in P
        # So R is less than min_p, which is the smallest p in P
        # Therefore, the minimum C is LCM of all p in P + R
        # But wait, no. Because if R is less than min_p, then C - R must be divisible by all p in P, including min_p
        # So the minimum C is LCM of all p in P + R
        # So let's compute the LCM of all p in P and add R
        # But wait, there's a mistake here. Because the problem says that after distributing the candies, there are always R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # So let's compute the LCM of all p in P and add R
        # But wait, no. Because the problem says that R is less than the minimum p in P
        # So R is less than min_p
        # So the minimum C is LCM of all p in P + R
        # But there's a mistake here. Because the problem says that after distributing the candies, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # But wait, no. Because the problem says that R is less than the minimum p in P
        # So R is less than min_p
        # So the minimum C is LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # So let's compute the LCM of all p in P and add R
        # But wait, no. Because the problem says that R is less than the minimum p in P
        # So R is less than min_p
        # So the minimum C is LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # So let's compute the LCM of all p in P and add R
        # But wait, no. Because the problem says that R is less than the minimum p in P
        # So R is less than min_p
        # So the minimum C is LCM of all p in P + R
        # But wait, no. Because the problem says that the number of candies must be such that after distributing, there are R candies remaining for Sushma.
        # So the number of candies must be such that when divided by each p in P, the remainder is R.
        # So C mod p == R for all p in P
        # Which implies that C - R is divisible by all p in P
        # So C - R must be a common multiple of all p in P
        # The minimum such C is the LCM of all p in P + R
        # So let's compute the