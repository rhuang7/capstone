import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    k = int(input[idx])
    idx += 1
    V = list(map(int, input[idx:idx+N]))
    idx += N
    B = list(map(int, input[idx:idx+N]))
    
    # Preprocess brackets to identify opening and closing
    opening = set(range(1, k+1))
    closing = set(range(k+1, 2*k+1))
    
    # dp[i][j] = maximum sum for a well-bracketed sequence ending with opening bracket i and closing bracket j
    dp = [[-float('inf')] * (k+1) for _ in range(k+1)]
    
    for i in range(N):
        if B[i] in opening:
            # Try to pair this opening bracket with a closing bracket later
            for j in range(i+1, N):
                if B[j] in closing and B[j] == B[i] + k:
                    # Check if the sequence is well-bracketed
                    # We need to ensure that the brackets are properly nested
                    # This is a simplified approach for the problem
                    # We'll use a stack to check if the sequence is well-bracketed
                    stack = []
                    valid = True
                    for m in range(i, j+1):
                        if B[m] in opening:
                            stack.append(B[m])
                        else:
                            if not stack or stack[-1] != B[m] - k:
                                valid = False
                                break
                            stack.pop()
                    if valid:
                        # Update dp
                        if dp[B[i]-1][B[j]-k] == -float('inf'):
                            dp[B[i]-1][B[j]-k] = V[i] + V[j]
                        else:
                            dp[B[i]-1][B[j]-k] = max(dp[B[i]-1][B[j]-k], V[i] + V[j])
    
    # Also consider single brackets (though they are not valid well-bracketed sequences)
    # So we need to find the maximum value among all valid pairs
    
    max_sum = -float('inf')
    for i in range(k):
        for j in range(k+1, 2*k+1):
            if dp[i][j - k] != -float('inf'):
                max_sum = max(max_sum, dp[i][j - k])
    
    print(max_sum)

if __name__ == '__main__':
    solve()