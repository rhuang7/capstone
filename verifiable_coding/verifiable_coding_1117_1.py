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
        
        compos = []
        for _ in range(Q):
            A = int(data[idx])
            B = int(data[idx+1])
            compos.append((A, B))
            idx += 2
        
        # For each player, compute the maximum skill
        # We'll use a prefix sum approach for each challenge
        # Since M is small, we can process all compos for each challenge
        
        # Initialize skill array
        skill = [0] * (N + 2)  # 1-based to N
        
        # For each challenge, compute which compos include it
        # And for each compo, track which challenges it includes
        # We'll use a 2D array: compo_challenges[comp][chall] = 1 if comp includes chall
        compo_challenges = [[0] * M for _ in range(Q)]
        
        for comp in range(Q):
            A, B = compos[comp]
            for chall in range(A-1, B):
                compo_challenges[comp][chall] = 1
        
        # For each challenge, collect all compos that include it
        # Then for each player, select the subset of compos that maximizes their skill
        # We can use a binary representation for the compos (since Q is up to 10,000, but M is small)
        # But since Q is up to 10,000 and M is small, we can use a greedy approach
        
        # For each challenge, collect all compos that include it
        challenge_compos = [[] for _ in range(M)]
        for comp in range(Q):
            A, B = compos[comp]
            for chall in range(A-1, B):
                challenge_compos[chall].append(comp)
        
        # For each challenge, we can select any subset of its compos
        # But we want to maximize the skill for each player
        # Since each challenge contributes X_i to the players in [L_i, R_i], we want to select the compos that include this challenge
        # For each player, we can select any subset of compos that include any challenge that affects them
        
        # We'll use a binary representation for the compos (since Q is up to 10,000, but M is small)
        # We'll use a bitmask for each player, where each bit represents whether a compo is selected
        # But since Q is up to 10,000, it's not feasible to store a bitmask for each player
        
        # Instead, for each player, we can collect all challenges that affect them, and then for each challenge, we can select any subset of compos that include it
        # The optimal selection is to select all compos that include any challenge that affects the player
        
        # For each player, we can collect all challenges that affect them
        # Then for each challenge, we can select all compos that include it
        # The maximum skill is the sum of X_i * (number of times the challenge is included in the selected compos)
        
        # We can use a greedy approach: for each challenge, include all compos that include it
        # Because including more compos increases the skill for the players in the challenge's range
        
        # So for each challenge, we include all compos that include it
        # Then for each player, the total skill is the sum of X_i for all challenges that include the player and are included in the compos
        
        # We'll use a prefix sum approach for each challenge
        # For each challenge, we'll add its X_i to the range [L_i, R_i]
        # But we need to consider which compos include this challenge
        
        # For each challenge, we'll add its X_i to the range [L_i, R_i] for all compos that include it
        # But since M is small, we can process all compos for each challenge
        
        # We'll use a 2D array: compo_effect on each challenge
        # But since M is small, we can process all compos for each challenge
        
        # For each challenge, we'll add its X_i to the range [L_i, R_i] for all compos that include it
        # We'll use a prefix sum array for each challenge
        # But since the same challenge can be included in multiple compos, we need to track how many times it is included
        
        # We'll use a 2D array: compo_effect for each challenge
        # compo_effect[chall] = number of times this challenge is included in the selected compos
        
        # But since we want to include all compos that include the challenge, we can just count how many compos include it
        
        # For each challenge, count how many compos include it
        compo_count = [0] * M
        for comp in range(Q):
            A, B = compos[comp]
            for chall in range(A-1, B):
                compo_count[chall] += 1
        
        # Now, for each challenge, we can add its X_i * compo_count[chall] to the range [L_i, R_i]
        # We'll use a prefix sum array for each player
        
        # Initialize a prefix sum array for each player
        # But since N is up to 1e5, we can use a single array and update it for each challenge
        
        # We'll use a difference array approach
        diff = [0] * (N + 2)
        
        for chall in range(M):
            L, R, X = challenges[chall]
            cnt = compo_count[chall]
            if cnt == 0:
                continue
            diff[L] += X * cnt
            diff[R + 1] -= X * cnt
        
        # Compute the prefix sum
        for i in range(1, N + 1):
            diff[i] += diff[i - 1]
        
        # The final skill array is the diff array
        results.append(' '.join(map(str, diff[1:N+1])))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()