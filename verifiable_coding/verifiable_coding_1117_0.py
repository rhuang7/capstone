import sys
import math

def main():
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
        
        # For each player, compute max skill
        # We'll use a difference array for challenges
        # Then for each composite, we'll compute the contribution to each challenge
        # Then we'll compute for each player the sum of all challenges they are in
        
        # Initialize a 2D array for challenge contribution
        # challenge_contribution[i][j] = contribution of challenge j to player i
        # But since M is small (up to 1000), we can precompute for each challenge
        # the range it affects, and then for each composite, compute the contribution
        # to each challenge, and then for each player, sum all challenges they are in
        
        # Precompute for each challenge, the range it affects
        # Then for each composite, compute the contribution to each challenge
        # Then for each player, sum all challenges they are in
        
        # For each challenge, create a difference array
        diff = [[0] * (N + 2) for _ in range(M)]
        
        for i in range(M):
            L, R, X = challenges[i]
            diff[i][L] += X
            diff[i][R + 1] -= X
        
        # Now, for each composite, compute the contribution to each challenge
        # and then for each player, sum all challenges they are in
        
        # For each composite, we'll compute the contribution to each challenge
        # and then for each player, sum all challenges they are in
        
        # For each composite, compute the contribution to each challenge
        # and then for each player, sum all challenges they are in
        
        # We'll use a 2D array to store the contribution of each composite to each challenge
        # Then for each player, we'll sum all challenges they are in
        
        # Initialize a 2D array for composite contribution
        # composite_contribution[i][j] = contribution of composite i to challenge j
        composite_contribution = [[0] * M for _ in range(Q)]
        
        for q in range(Q):
            A, B = composites[q]
            for i in range(A - 1, B):
                composite_contribution[q][i] = 1
        
        # Now, for each player, compute the total contribution
        # We'll use a 1D array to store the total contribution for each player
        total = [0] * (N + 2)
        
        for q in range(Q):
            for i in range(M):
                if composite_contribution[q][i]:
                    # Add the contribution of challenge i to each player
                    for j in range(N + 1):
                        total[j] += diff[i][j]
        
        # Now, for each player, the total is the sum of all challenges they are in
        # So we can just output total[1...N]
        res = [str(total[i]) for i in range(1, N + 1)]
        results.append(' '.join(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()