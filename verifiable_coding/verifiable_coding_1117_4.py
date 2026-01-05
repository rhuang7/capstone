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
        # We'll use a difference array for the challenges
        # Then for each compo, we'll add it to a list of ranges
        # Then for each player, we'll find which composes include them
        # But since the number of composes is up to 10,000 and N is up to 1e5, we need an efficient way
        
        # First, for each challenge, we'll record which composes include it
        # Then for each player, we'll find all composes that include them and sum the challenges in those composes
        # But since each compo is a range of challenges, we can precompute for each compo the list of challenges it includes
        # Then for each player, we'll find all composes that include them, and sum the challenges in those composes
        
        # Precompute for each compo the list of challenges it includes
        compo_challenges = []
        for A, B in composes:
            compo_challenges.append(set(range(A-1, B)))
        
        # For each challenge, record which composes include it
        compo_includes = [set() for _ in range(M)]
        for i in range(Q):
            A, B = composes[i]
            for j in range(A-1, B):
                compo_includes[j].add(i)
        
        # For each player, we'll find all composes that include them, and sum the challenges in those composes
        # To do this efficiently, we can for each player, find all composes that include them, and for each such compo, add the challenges in that compo
        # But this would be O(Q*N), which is too slow for N=1e5 and Q=1e4
        
        # Instead, we can precompute for each compo the list of challenges it includes, and for each challenge, record which composes include it
        # Then for each player, we can iterate over all challenges that include them, and for each such challenge, add the sum of composes that include it
        
        # Precompute for each challenge, the sum of all composes that include it
        # But since each compo is a range of challenges, we can precompute for each compo the sum of X_i for the challenges in it
        # Then for each player, we can find all composes that include them, and sum the sum of X_i for those composes
        
        # Precompute for each compo the sum of X_i for the challenges in it
        compo_sum = [0] * Q
        for i in range(Q):
            A, B = composes[i]
            total = 0
            for j in range(A-1, B):
                total += challenges[j][2]
            compo_sum[i] = total
        
        # Now, for each player, we need to find all composes that include them, and sum the compo_sum of those composes
        # To do this efficiently, we can for each player, find all composes that include them, and sum the compo_sum of those composes
        
        # To find all composes that include a player, we can for each compo, record the range of players it includes
        # Then for each player, we can find all composes that include them
        # But this would be O(Q*N), which is too slow for N=1e5 and Q=1e4
        
        # Instead, we can for each compo, record the range of players it includes, and then for each player, we can find all composes that include them
        # But again, this would be O(Q*N), which is too slow
        
        # So we need a better approach
        
        # Let's think differently: for each challenge, we can record which composes include it
        # Then for each player, we can find all challenges that include them, and for each such challenge, add the sum of composes that include it
        
        # So for each challenge, we can compute the sum of all composes that include it
        # Then for each player, we can sum all challenges that include them, and for each such challenge, add the sum of composes that include it
        
        # Let's precompute for each challenge, the sum of all composes that include it
        challenge_compo_sum = [0] * M
        for i in range(M):
            for compo in compo_includes[i]:
                challenge_compo_sum[i] += compo_sum[compo]
        
        # Now, for each player, we can find all challenges that include them, and sum the challenge_compo_sum of those challenges
        # To find all challenges that include a player, we can use a prefix sum array
        
        # Create a prefix sum array for each player
        # For each challenge, we can add its contribution to the range [L, R]
        # Then for each player, we can query the prefix sum array to get the total contribution
        
        # Initialize a difference array for the challenges
        diff = [0] * (N + 2)
        for i in range(M):
            L, R, X = challenges[i]
            diff[L] += challenge_compo_sum[i]
            diff[R + 1] -= challenge_compo_sum[i]
        
        # Compute the prefix sum to get the total contribution for each player
        res = [0] * N
        current = 0
        for i in range(1, N + 1):
            current += diff[i]
            res[i - 1] = current
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))