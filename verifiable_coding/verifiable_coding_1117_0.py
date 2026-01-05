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
        composes = []
        for _ in range(Q):
            A = int(data[idx])
            B = int(data[idx+1])
            composes.append((A, B))
            idx += 2
        
        # For each player, compute the maximum skill
        # We will use a prefix sum approach for each challenge
        # Since M is small, we can precompute for each challenge
        # the contribution to each player, then for each compo,
        # we can add the contribution of the challenges in that compo
        # to the players
        
        # Initialize skill array
        skill = [0] * (N + 2)  # 1-based indexing
        
        # For each challenge, we will create a delta array
        # that represents the contribution to each player
        # We will use a difference array approach to apply the range updates
        # Then, after all challenges are processed, we will compute the prefix sum
        # to get the total contribution of each challenge to each player
        
        # Create a difference array for each challenge
        # Since M is small, we can do this efficiently
        delta = [ [0]*(N+2) for _ in range(M) ]
        
        for i in range(M):
            L, R, X = challenges[i]
            delta[i][L] += X
            delta[i][R+1] -= X
        
        # Now, for each compo, we will add the contribution of the challenges in that compo
        # to the players
        # We will use a prefix sum approach for each compo
        # Since Q is up to 10,000 and M is up to 1,000, this is feasible
        
        # For each compo, we will create a temporary array that represents the contribution
        # of the challenges in that compo to each player
        # Then, we will add this to the skill array
        
        for compo in composes:
            A, B = compo
            # Create a temporary array for this compo
            temp = [0]*(N+2)
            for i in range(A-1, B):
                for j in range(1, N+1):
                    temp[j] += delta[i][j]
            # Now, compute prefix sum of temp to get the contribution to each player
            prefix = [0]*(N+2)
            for j in range(1, N+1):
                prefix[j] = prefix[j-1] + temp[j]
            # Add this to the skill array
            for j in range(1, N+1):
                skill[j] += prefix[j]
        
        # Now, compute the final skill for each player
        result = []
        for i in range(1, N+1):
            result.append(str(skill[i]))
        results.append(' '.join(result))
    
    print('\n'.join(results))