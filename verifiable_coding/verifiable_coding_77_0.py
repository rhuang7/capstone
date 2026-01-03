import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        boards = []
        for _ in range(n):
            a = int(data[idx])
            b = int(data[idx+1])
            boards.append((a, b))
            idx += 2
        
        # For each board, we can choose to increase it 0, 1, or 2 times
        # We need to ensure that adjacent boards have different heights
        # We'll use dynamic programming to track the minimum cost for each possible height
        
        # For each board, we'll track the minimum cost if the board has height 0, 1, or 2 more than original
        # But since we can increase it any number of times, we can only consider the next two possible heights
        # Because if we increase it more than 2 times, it will be equal to the next board's height (if not increased)
        
        # Initialize dp for the first board
        dp = [0] * 3
        for i in range(3):
            dp[i] = boards[0][1] * i
        
        for i in range(1, n):
            new_dp = [float('inf')] * 3
            a_i, b_i = boards[i]
            for prev in range(3):
                for curr in range(3):
                    if prev != curr:
                        cost = dp[prev] + b_i * (curr - a_i)
                        if cost < new_dp[curr]:
                            new_dp[curr] = cost
            dp = new_dp
        
        results.append(min(dp))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()