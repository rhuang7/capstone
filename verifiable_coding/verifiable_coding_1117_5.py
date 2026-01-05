import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        Q = int(data[idx+2])
        idx += 3
        
        challenges = []
        for _ in range(M):
            L = int(data[idx])
            R = int(data[idx+1])
            X = int(data[idx+2])
            challenges.append((L, R, X))
            idx += 3
        
        composites = []
        for _ in range(Q):
            A = int(data[idx])
            B = int(data[idx+1])
            composites.append((A, B))
            idx += 2
        
        # For each player, compute the maximum skill
        # We'll use a difference array for the challenges
        # Then for each compo, we'll compute the effect on the challenges
        # And then for each player, we'll compute the total effect
        
        # Initialize the skill array
        skill = [0] * (N + 2)  # 1-based indexing
        
        # For each compo, compute the effect on the challenges
        # We'll use a difference array for the challenges
        # Then for each challenge, we'll compute how many times it is included in the composites
        # And then for each player, we'll compute the total effect
        
        # We'll use a difference array for the challenges
        diff = [0] * (M + 2)
        
        for compo in composites:
            A, B = compo
            diff[A] += 1
            diff[B + 1] -= 1
        
        # Compute the number of times each challenge is included in the composites
        cnt = [0] * (M + 2)
        for i in range(1, M + 1):
            cnt[i] = cnt[i - 1] + diff[i]
        
        # Now, for each challenge, compute the total contribution to each player
        # We'll use a difference array for the players
        res = [0] * (N + 2)
        
        for i in range(M):
            L, R, X = challenges[i]
            if cnt[i + 1] == 0:
                continue
            # The challenge is included in cnt[i+1] composites
            # So its total contribution is X * cnt[i+1]
            # We apply this to the players L to R
            res[L] += X * cnt[i + 1]
            res[R + 1] -= X * cnt[i + 1]
        
        # Compute the prefix sum for the players
        for i in range(1, N + 1):
            res[i] += res[i - 1]
        
        # Extract the results for players 1 to N
        results.append(' '.join(map(str, res[1:N+1])))
    
    print('\n'.join(results))