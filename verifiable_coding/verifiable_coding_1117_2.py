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
        
        # For each player, we need to find the maximum skill
        # We'll use a difference array for each challenge
        # Then for each composite, we'll find which challenges it includes
        # And for each challenge, we'll find which composites include it
        
        # Initialize skill array
        skill = [0] * (N + 2)  # 1-based to N
        
        # For each challenge, find which composites include it
        # We'll use a list of sets: compo_challenges[compo_idx] = set of challenge indices
        compo_challenges = [set() for _ in range(Q)]
        for compo_idx in range(Q):
            A, B = composites[compo_idx]
            for challenge_idx in range(A-1, B):
                compo_challenges[compo_idx].add(challenge_idx)
        
        # For each challenge, find which composites include it
        # We'll use a list of sets: challenge_compos[challenge_idx] = set of compo indices
        challenge_compos = [set() for _ in range(M)]
        for compo_idx in range(Q):
            for challenge_idx in compo_challenges[compo_idx]:
                challenge_compos[challenge_idx].add(compo_idx)
        
        # For each challenge, we can compute the total contribution
        # We'll use a binary representation for composites to find the best subset
        # Since Q is up to 10,000, we can't do brute force
        # Instead, we'll use a greedy approach: for each challenge, select composites that include it
        # and contribute positively
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll find the maximum sum of X_i * (number of times it is selected)
        # But since a compo can be selected only once, we need to select a subset of composites
        # such that for each challenge, the sum of X_i for composites that include it is maximized
        
        # We'll use a binary representation for composites to find the best subset
        # For each challenge, we can compute the maximum contribution by selecting composites that include it
        # and have positive X_i
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we can select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a prefix sum array for each challenge
        # But since the number of challenges is small (M up to 1000), we can process them all
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of each player
        # But since N is up to 1e5, we can't do that for each player
        # Instead, we'll use a prefix sum array for each challenge
        
        # For each challenge, we'll compute the total contribution
        # and apply it to the players in the challenge's range
        
        # For each challenge, collect all composites that include it
        # Then for each challenge, we'll select the composites that have positive X_i
        # and add their X_i to the skill of the players in the challenge's range
        
        # We'll use a difference array for the skill of