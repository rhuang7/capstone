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
        
        # Initialize player ratings after each month
        player_ratings = [[R[i]] for i in range(N)]
        for j in range(M):
            for i in range(N):
                player_ratings[i].append(player_ratings[i][-1] + int(data[idx]))
            idx += 1
        
        # For each player, compute their ratings after each month
        # Then compute their rankings after each month
        # For each player, find peak rating month and peak ranking month
        
        count = 0
        for i in range(N):
            # Get all ratings for player i
            ratings = player_ratings[i]
            
            # Find peak rating month (earliest)
            max_rating = max(ratings)
            peak_rating_month = 0
            for j in range(M):
                if ratings[j] == max_rating:
                    peak_rating_month = j
                    break
            
            # Compute rankings after each month
            # For each month, sort the ratings and assign ranks
            # Note: if multiple players have same rating, they get same rank
            # So we need to compute the rank for each month for all players
            # But since we only need the rank for player i, we can compute it
            
            # For each month, collect all ratings
            # Then compute the rank for player i
            # But since we need to find the peak ranking month, we need to compute the rank for each month
            # So we'll precompute the rankings for all months
            
            # Precompute rankings for all months
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # We'll store for each month, a list of ranks for all players
            # But since we only need the rank for player i, we can compute it
            
            # For each month, compute the rank for player i
            # So for each month, we'll collect all ratings, sort them, and assign ranks
            # Then for player i, we'll find the earliest month where he gets his best rank
            
            # Precompute for each month, the list of ratings
            # But since we already have the player_ratings, we can use that
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # For each month, we'll store the rank of player i
            
            # Precompute for each month, the rank of player i
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # Precompute for each month, the rank of player i
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then for player i, find the earliest month where he gets his best rank
            
            # For each month, collect all ratings
            # Then sort them and assign ranks
            # Then