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
        
        rating_changes = []
        for _ in range(N):
            rating_changes.append(list(map(int, data[idx:idx+M])))
            idx += M
        
        # Compute final ratings for each player
        final_ratings = []
        for i in range(N):
            rating = R[i]
            for j in range(M):
                rating += rating_changes[i][j]
            final_ratings.append(rating)
        
        # For each player, compute their ratings after each month
        player_ratings = []
        for i in range(N):
            ratings = [R[i]]
            for j in range(M):
                ratings.append(ratings[-1] + rating_changes[i][j])
            player_ratings.append(ratings)
        
        # For each month, compute the rankings
        month_rankings = []
        for j in range(M):
            month_ratings = [player_ratings[i][j+1] for i in range(N)]
            # Sort the ratings and assign ranks
            sorted_ratings = sorted(month_ratings)
            rank = 1
            prev = None
            rank_dict = {}
            for i in range(N):
                if month_ratings[i] != prev:
                    rank = i + 1
                    prev = month_ratings[i]
                rank_dict[i] = rank
            month_rankings.append(rank_dict)
        
        # For each player, find peak rating month and peak ranking month
        count = 0
        for i in range(N):
            # Find peak rating month
            max_rating = -float('inf')
            peak_rating_month = 0
            for j in range(M):
                if player_ratings[i][j+1] > max_rating:
                    max_rating = player_ratings[i][j+1]
                    peak_rating_month = j
                elif player_ratings[i][j+1] == max_rating:
                    if j < peak_rating_month:
                        peak_rating_month = j
            
            # Find peak ranking month
            best_rank = float('inf')
            peak_ranking_month = 0
            for j in range(M):
                rank = month_rankings[j][i]
                if rank < best_rank:
                    best_rank = rank
                    peak_ranking_month = j
                elif rank == best_rank:
                    if j < peak_ranking_month:
                        peak_ranking_month = j
            
            if peak_rating_month != peak_ranking_month:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()