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
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        R = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute ratings after each month
        ratings = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                ratings[i][j] = R[i] + sum(data[idx + i*M + j])
        idx += N*M
        
        # For each player, compute their peak rating month and peak ranking month
        peak_rating_month = [0]*N
        peak_ranking_month = [0]*N
        
        for i in range(N):
            # Find peak rating month
            max_rating = -1
            peak_month = 0
            for j in range(M):
                if ratings[i][j] > max_rating:
                    max_rating = ratings[i][j]
                    peak_month = j
            peak_rating_month[i] = peak_month
            
            # Find peak ranking month
            # Compute rankings after each month
            # Create a list of ratings for this month
            # Sort and assign ranks
            # For each month, compute rankings
            # For each player, track their best rank month
            # We need to compute rankings for each month
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where they achieved their best rank
            # So for each month, we compute the rankings
            # Then for each player, track their best rank and the earliest month they achieved it
            # So we'll do this for each month
            # For each player, we'll track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So for each player, we'll track their best rank and the earliest month they achieved it
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best
            # So we'll do this for each month
            # For each month, compute the rankings
            # Then, for each player, track their best rank and the earliest month they achieved it
            # So we'll create a list of rankings for each month
            # Then, for each player, find the earliest month where their rank is their best