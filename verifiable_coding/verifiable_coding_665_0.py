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
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        R = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Initialize player ratings
        player_ratings = []
        for _ in range(N):
            rating = R.copy()
            player_ratings.append(rating)
        
        # Apply changes for each month
        for month in range(M):
            for i in range(N):
                player_ratings[i][month] += int(data[idx])
            idx += 1
        
        # For each player, compute their ratings after each month
        # And compute their rankings after each month
        # Then find peak rating month and peak ranking month
        
        peak_rating_months = []
        peak_ranking_months = []
        
        for i in range(N):
            # Compute ratings for each month
            ratings = [player_ratings[i][j] for j in range(M)]
            
            # Find peak rating month (earliest)
            max_rating = max(ratings)
            peak_rating_month = 0
            for j in range(M):
                if ratings[j] == max_rating:
                    peak_rating_month = j
                    break
            
            # Compute rankings for each month
            # For each month, sort the ratings and assign ranks
            # If multiple players have the same rating, they share the same rank
            rankings = []
            for j in range(M):
                current_ratings = [player_ratings[k][j] for k in range(N)]
                sorted_ratings = sorted(current_ratings, reverse=True)
                rank = 1
                for k in range(N):
                    if current_ratings[k] != sorted_ratings[k]:
                        break
                    rank += 1
                rankings.append(rank)
            
            # Find peak ranking month (earliest)
            max_rank = max(rankings)
            peak_ranking_month = 0
            for j in range(M):
                if rankings[j] == max_rank:
                    peak_ranking_month = j
                    break
            
            # Check if peak rating month and peak ranking month are the same
            if peak_rating_month != peak_ranking_month:
                results.append(1)
            else:
                results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()