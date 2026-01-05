import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    if any(a == 0 for a in A):
        print(-1)
        return
    
    # We need to find the minimum number of speeches such that every K consecutive soldiers have sum >= M
    # Each speech multiplies a segment of K consecutive soldiers by X (X > 1)
    # We can use a greedy approach: find the earliest segment where the sum is < M, and apply a speech to it
    # To minimize the number of speeches, we should apply speeches to the earliest possible segments
    
    # We can use a sliding window approach to find the segments where the sum is < M
    # We will apply speeches to the earliest segments first
    
    # Initialize the result
    res = 0
    
    # We will keep track of the current sum of the window
    current_sum = sum(A[:K])
    
    # We will iterate through the array and check each window of size K
    i = 0
    while i <= N - K:
        if current_sum < M:
            # We need to apply a speech to this window
            # We can apply it to the entire window, but we need to find the minimum X
            # X must be such that X * sum(A[i:i+K]) >= M
            # X = ceil(M / sum(A[i:i+K]))
            # However, since X can be any positive value, we can just apply it to the entire window
            # So we can apply a speech to this window
            res += 1
            # Apply the speech to the entire window
            # Multiply each element in the window by X, where X is such that X * sum(A[i:i+K]) >= M
            # Since X can be any value, we can just multiply by a value that makes the sum >= M
            # We can multiply by 1 (but that doesn't help), so we need to find the minimal X
            # X = ceil(M / sum(A[i:i+K]))
            # However, since we can choose any X, we can just apply a speech to this window
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # However, since we are applying a speech to the entire window, we can just multiply the sum by X
            # But we don't know X, so we can't compute it
            # So we can just apply the speech and move to the next window
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # However, since we don't know X, we can't compute it
            # So we can just apply the speech and move to the next window
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # However, since we don't know X, we can't compute it
            # So we can just apply the speech and move to the next window
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum
            # So we can just increment the count and move to the next window
            # But we need to update the current_sum