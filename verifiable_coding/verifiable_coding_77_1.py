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
            b = int(data[idx + 1])
            idx += 2
            boards.append((a, b))
        
        if n == 1:
            results.append(0)
            continue
        
        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            a_prev, b_prev = boards[i - 1]
            a_curr, b_curr = boards[i]
            
            if a_prev != a_curr:
                dp[i] = dp[i - 1]
            else:
                # We need to change either the previous or current board
                # Try increasing the previous board by 1
                cost_prev = dp[i - 1] + b_prev
                # Try increasing the current board by 1
                cost_curr = dp[i - 1] + b_curr
                # Try increasing the previous board by 2
                cost_prev2 = dp[i - 1] + 2 * b_prev
                # Try increasing the current board by 2
                cost_curr2 = dp[i - 1] + 2 * b_curr
                # Try increasing the previous board by 1 and current by 1
                cost_prev_curr = dp[i - 1] + b_prev + b_curr
                # Try increasing the previous board by 2 and current by 1
                cost_prev_curr2 = dp[i - 1] + 2 * b_prev + b_curr
                # Try increasing the previous board by 1 and current by 2
                cost_prev_curr3 = dp[i - 1] + b_prev + 2 * b_curr
                # Try increasing the previous board by 2 and current by 2
                cost_prev_curr4 = dp[i - 1] + 2 * b_prev + 2 * b_curr
                # Choose the minimum cost
                dp[i] = min(cost_prev, cost_curr, cost_prev2, cost_curr2, cost_prev_curr, cost_prev_curr2, cost_prev_curr3, cost_prev_curr4)
        
        results.append(dp[-1])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()