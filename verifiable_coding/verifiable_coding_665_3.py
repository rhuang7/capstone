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
        
        # Initialize player ratings
        player_ratings = []
        for i in range(N):
            rating = R[i]
            curr = [rating]
            for j in range(M):
                rating += int(data[idx])
                curr.append(rating)
                idx += 1
            player_ratings.append(curr)
        
        # For each player, compute peak rating month and peak ranking month
        count = 0
        for i in range(N):
            # Find peak rating month
            max_rating = -1
            peak_rating_month = 0
            for j in range(M):
                if player_ratings[i][j] > max_rating:
                    max_rating = player_ratings[i][j]
                    peak_rating_month = j
                elif player_ratings[i][j] == max_rating:
                    if j < peak_rating_month:
                        peak_rating_month = j
            
            # Find peak ranking month
            # Compute rankings for each month
            rankings = []
            for j in range(M):
                # Get ratings for this month
                ratings = [player_ratings[k][j] for k in range(N)]
                # Sort ratings and assign ranks
                sorted_ratings = sorted(ratings)
                # Assign ranks
                rank = 1
                prev = None
                for r in sorted_ratings:
                    if r != prev:
                        prev = r
                        rank = sorted_ratings.index(r) + 1
                rankings.append(rank)
            
            # Find peak ranking month
            min_rank = float('inf')
            peak_ranking_month = 0
            for j in range(M):
                if rankings[j] < min_rank:
                    min_rank = rankings[j]
                    peak_ranking_month = j
                elif rankings[j] == min_rank:
                    if j < peak_ranking_month:
                        peak_ranking_month = j
            
            if peak_rating_month != peak_ranking_month:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()