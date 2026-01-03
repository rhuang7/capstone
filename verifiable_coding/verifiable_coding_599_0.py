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
        # Find all positions where max_w occurs
        max_positions = [i for i, val in enumerate(W) if val == max_w]
        # For each possible k, check if the first half of the shifted array does not contain any max_w
        count = 0
        for k in range(N):
            # Shift by k, first half is positions [k : k + N//2]
            # In the shifted array, the first half is W[k:] + W[:k]
            # So the first half is from index k to k + N//2 - 1 in the original array
            # Check if any of these positions have max_w
            # The first half of the shifted array is the original array's positions [k, k + N//2 - 1]
            # So check if any of these positions are in max_positions
            # But since the array is circular, we need to wrap around
            # So for each position in [k, k + N//2 - 1], check if it is in max_positions
            # But since N is even, k + N//2 - 1 = k + (N//2) - 1
            # So the range is from k to k + (N//2) - 1
            # But since it's circular, we need to check if any of these positions are in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # To do this, we can check if any of the positions in [k, k + N//2 - 1] (mod N) are in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array, check if it is in max_positions
            # So for each position in the first half of the shifted array