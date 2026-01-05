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
            a_i, b_i = boards[i]
            a_prev, b_prev = boards[i - 1]
            
            if a_prev != a_i:
                dp[i] = dp[i - 1]
            else:
                # Need to change either current or previous
                # Try increasing current by 1
                cost1 = dp[i - 1] + b_i
                # Try increasing previous by 1
                cost2 = dp[i - 2] + b_prev if i > 1 else 0 + b_prev
                dp[i] = min(cost1, cost2)
        
        results.append(dp[-1])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()