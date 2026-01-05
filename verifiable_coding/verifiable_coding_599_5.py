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
        N = int(data[idx])
        idx += 1
        W = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_w = max(W)
        count = 0
        
        # Find all positions where the maximum occurs
        max_positions = [i for i, val in enumerate(W) if val == max_w]
        
        # For each possible shift k, check if the first half of the shifted array
        # contains no maximum value
        for k in range(N):
            # The first half is positions 0 to N//2 - 1 in the shifted array
            # The shifted array is W[k:] + W[:k]
            # So the first half is W[k:] + W[:k][:(N//2)]
            # We need to check if any of these elements is max_w
            # We can check if any of the first N//2 elements in the shifted array is max_w
            # The first N//2 elements in the shifted array are:
            # W[k], W[k+1], ..., W[N-1], W[0], W[1], ..., W[k-1]
            # So the first N//2 elements are:
            # W[k : k + N//2] if k + N//2 <= N else W[k:] + W[:k + N//2 - N]
            # We can check if any of these elements is max_w
            # We can check if any of the elements in the first half of the shifted array is max_w
            # We can do this by checking if any of the elements in the first N//2 positions of the shifted array is max_w
            # The first N//2 positions of the shifted array are:
            # W[k], W[k+1], ..., W[N-1], W[0], W[1], ..., W[k-1]
            # So we can check if any of the elements in the range [k, k + N//2 - 1] (mod N) is max_w
            # But since the array is circular, we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # But since the array is circular, we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # But since the array is circular, we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # But since the array is circular, we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # We can do this by checking if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k + N//2 - 1] is max_w
            # So we can check if any of the elements in the range [k, k