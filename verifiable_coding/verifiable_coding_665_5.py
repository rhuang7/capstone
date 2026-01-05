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
            # Get ratings for this month
            month_ratings = [ratings[i][j] for i in range(N)]
            # Sort with stable sort to get ranks
            sorted_ratings = sorted(enumerate(month_ratings), key=lambda x: (-x[1], x[0]))
            # Assign ranks
            rank = 1
            prev = -1
            for k in range(N):
                if sorted_ratings[k][1] != prev:
                    prev = sorted_ratings[k][1]
                    rank = k + 1
                rankings[sorted_ratings[k][0]][j] = rank
        
        # For each player, find peak rating month and peak ranking month
        count = 0
        for i in range(N):
            # Find peak rating month
            max_rating = -1
            peak_rating_month = 0
            for j in range(M):
                if ratings[i][j] > max_rating:
                    max_rating = ratings[i][j]
                    peak_rating_month = j
                elif ratings[i][j] == max_rating:
                    if j < peak_rating_month:
                        peak_rating_month = j
            # Find peak ranking month
            max_rank = float('inf')
            peak_ranking_month = 0
            for j in range(M):
                if rankings[i][j] < max_rank:
                    max_rank = rankings[i][j]
                    peak_ranking_month = j
                elif rankings[i][j] == max_rank:
                    if j < peak_ranking_month:
                        peak_ranking_month = j
            # Check if months are different
            if peak_rating_month != peak_ranking_month:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()