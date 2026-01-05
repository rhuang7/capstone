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
        # Find all positions where the maximum occurs
        max_positions = [i for i, val in enumerate(W) if val == max_w]
        # For each possible shift k, check if the first half of the shifted array
        # does not contain any maximum value
        count = 0
        for k in range(N):
            # Shift by k, the first half is positions [k : k + N//2]
            # In the shifted array, the first half is the elements from k to k + N//2 - 1
            # In the original array, this corresponds to the elements from k to N-1 and 0 to (N//2 - 1 - k) if k > N//2
            # So we need to check if any of the max_positions are in the first half
            # So for each max position i, check if it is in the first half of the shifted array
            # The first half of the shifted array is the first N//2 elements
            # So the positions in the original array that are in the first half of the shifted array are:
            # For k in 0..N-1:
            # The first half of the shifted array is [k, k+1, ..., k + N//2 - 1] mod N
            # So the positions in the original array that are in the first half of the shifted array are:
            # For each position i in the original array, it is in the first half of the shifted array if:
            # (i - k) mod N < N//2
            # Which is equivalent to i - k < N//2 or i - k >= N//2 and i - k + N < N//2
            # Which is equivalent to i < k + N//2 or i >= k + N//2 and i < k + N//2 + N
            # Which simplifies to i < k + N//2 or i >= k + N//2 and i < k + N//2 + N
            # Which is always true, so the first half of the shifted array is the first N//2 elements of the shifted array
            # So the first half of the shifted array is the elements from k to k + N//2 - 1 (mod N)
            # So the positions in the original array that are in the first half of the shifted array are:
            # For i in 0..N-1:
            # if (i - k) % N < N//2
            # So for each max position i, check if (i - k) % N < N//2
            # If any of them is true, then this shift is invalid
            # So for a shift k to be valid, none of the max positions i should satisfy (i - k) % N < N//2
            valid = True
            for i in max_positions:
                if (i - k) % N < N // 2:
                    valid = False
                    break
            if valid:
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()