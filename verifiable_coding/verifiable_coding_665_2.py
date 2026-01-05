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
        
        # Compute rankings after each month
        rankings = [[0]*M for _ in range(N)]
        for j in range(M):
            month_ratings = [ratings[i][j] for i in range(N)]
            sorted_ratings = sorted(month_ratings)
            rank = 1
            for i in range(N):
                if i > 0 and month_ratings[i] != sorted_ratings[i-1]:
                    rank = i + 1
                rankings[i][j] = rank
        
        # For each player, find peak rating month and peak ranking month
        count = 0
        for i in range(N):
            # Find peak rating month
            max_rating = -float('inf')
            peak_rating_month = 0
            for j in range(M):
                if ratings[i][j] > max_rating:
                    max_rating = ratings[i][j]
                    peak_rating_month = j
                elif ratings[i][j] == max_rating and j < peak_rating_month:
                    peak_rating_month = j
            
            # Find peak ranking month
            min_rank = float('inf')
            peak_ranking_month = 0
            for j in range(M):
                if rankings[i][j] < min_rank:
                    min_rank = rankings[i][j]
                    peak_ranking_month = j
                elif rankings[i][j] == min_rank and j < peak_ranking_month:
                    peak_ranking_month = j
            
            if peak_rating_month != peak_ranking_month:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()