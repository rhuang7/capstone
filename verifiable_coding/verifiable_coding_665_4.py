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
        
        # Compute ratings after each month
        ratings = []
        for i in range(N):
            current_rating = R[i]
            ratings.append([current_rating])
            for j in range(M):
                current_rating += rating_changes[i][j]
                ratings[i].append(current_rating)
        
        # Compute rankings after each month
        rankings = []
        for month in range(M):
            month_ratings = [ratings[i][month+1] for i in range(N)]
            sorted_ratings = sorted(month_ratings)
            rank_dict = {}
            for i in range(N):
                if month_ratings[i] != sorted_ratings[0]:
                    rank_dict[month_ratings[i]] = len(rank_dict) + 1
                else:
                    rank_dict[month_ratings[i]] = 1
            rank_list = [rank_dict[month_ratings[i]] for i in range(N)]
            rankings.append(rank_list)
        
        # For each player, find peak rating month and peak ranking month
        count = 0
        for i in range(N):
            # Find peak rating month
            max_rating = -float('inf')
            peak_rating_month = 0
            for j in range(M):
                if ratings[i][j+1] > max_rating:
                    max_rating = ratings[i][j+1]
                    peak_rating_month = j
                elif ratings[i][j+1] == max_rating:
                    if j < peak_rating_month:
                        peak_rating_month = j
            
            # Find peak ranking month
            min_rank = float('inf')
            peak_ranking_month = 0
            for j in range(M):
                if rankings[j][i] < min_rank:
                    min_rank = rankings[j][i]
                    peak_ranking_month = j
                elif rankings[j][i] == min_rank:
                    if j < peak_ranking_month:
                        peak_ranking_month = j
            
            if peak_rating_month != peak_ranking_month:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()