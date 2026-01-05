import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        S = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Precompute 2^p for all p in A
        power = [1 << p for p in A]
        
        # Since players play optimally, this is a game of Grundy numbers
        # We calculate the Grundy number for each position in the stack
        # The game is a variant of the Nim game, but with moves based on the set S
        
        # We will use memoization to compute the Grundy number for each position
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def grundy(pos):
            if pos == N:
                return 0
            res = 0
            for x in S:
                if x <= pos:
                    g = grundy(pos - x)
                    res |= g
            return res
        
        # The overall Grundy number of the game is grundy(N)
        g = grundy(N)
        
        # If the Grundy number is 0, the second player (Garry) wins
        # Otherwise, the first player (Chef) wins
        if g == 0:
            results.append("Garry")
        else:
            results.append("Chef")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()