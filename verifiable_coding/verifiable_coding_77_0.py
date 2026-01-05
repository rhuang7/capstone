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
            boards.append((a, b))
            idx += 2
        
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
                dp[i] = dp[i - 1] + b_curr
                
                if i > 1:
                    a_prev_prev, b_prev_prev = boards[i - 2]
                    if a_prev_prev != a_curr:
                        dp[i] = min(dp[i], dp[i - 2] + b_curr)
                    else:
                        dp[i] = min(dp[i], dp[i - 2] + b_curr)
        
        results.append(dp[-1])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()