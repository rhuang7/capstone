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
        # For each player, find the maximum skill
        # We'll use a difference array for the challenges
        # Then for each compo, we'll add it to the range of challenges
        # Finally, we'll compute the prefix sum for each player
        # Initialize the skill array
        skill = [0] * (N + 2)  # 1-based to N
        # For each compo, we'll add it to the range of challenges
        # We'll use a difference array for the composites
        compo_diff = [0] * (M + 2)  # 1-based to M
        for i in range(Q):
            A, B = composites[i]
            compo_diff[A] += 1
            compo_diff[B + 1] -= 1
        # Compute the prefix sum for the compo counts
        compo_count = [0] * (M + 1)
        for i in range(1, M + 1):
            compo_count[i] = compo_count[i - 1] + compo_diff[i]
        # Now, for each challenge, we'll apply it to the players
        # We'll use a difference array for the challenges
        challenge_diff = [0] * (N + 2)  # 1-based to N
        for i in range(M):
            L, R, X = challenges[i]
            # The challenge is included in compo_count[i] composites
            # So we add X * compo_count[i] to the range [L, R]
            challenge_diff[L] += X * compo_count[i]
            challenge_diff[R + 1] -= X * compo_count[i]
        # Compute the prefix sum for the skill
        for i in range(1, N + 1):
            skill[i] += skill[i - 1] + challenge_diff[i]
        # Output the skill for each player
        results.append(' '.join(map(str, skill[1:N+1])))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()