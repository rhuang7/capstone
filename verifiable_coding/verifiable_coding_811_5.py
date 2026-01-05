import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+N]))
    
    # dp_forward[i] = max score to reach i from k in forward phase
    dp_forward = [float('-inf')] * (N + 2)
    dp_forward[k] = 0
    for i in range(k, N):
        dp_forward[i + 1] = max(dp_forward[i + 1], dp_forward[i] + a[i + 1])
        if i + 2 <= N:
            dp_forward[i + 2] = max(dp_forward[i + 2], dp_forward[i] + a[i + 2])
    
    # dp_backward[i] = max score to reach i from N in backward phase
    dp_backward = [float('-inf')] * (N + 2)
    dp_backward[N] = 0
    for i in range(N, 0, -1):
        dp_backward[i - 1] = max(dp_backward[i - 1], dp_backward[i] + a[i - 1])
        if i - 2 >= 1:
            dp_backward[i - 2] = max(dp_backward[i - 2], dp_backward[i] + a[i - 2])
    
    # The answer is the max score from k to N in forward phase and then back to 1 in backward phase
    max_score = float('-inf')
    for i in range(1, N + 1):
        if dp_forward[i] != float('-inf') and dp_backward[i] != float('-inf'):
            total = dp_forward[i] + dp_backward[i]
            if total > max_score:
                max_score = total
    print(max_score)

if __name__ == '__main__':
    solve()