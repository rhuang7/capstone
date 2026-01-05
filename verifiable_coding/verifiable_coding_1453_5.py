import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    S = data[idx]
    
    # Preprocess the array to handle rotations
    # We'll keep track of the current rotation offset
    # For example, if we have rotated right once, the array is shifted right by 1
    # So the original array is A[0], A[1], ..., A[N-1]
    # After one rotation, it's A[N-1], A[0], A[1], ..., A[N-2]
    # So for any rotation offset 'rot', the effective array is A[rot], A[rot+1], ..., A[N-1], A[0], A[1], ..., A[rot-1]
    # To handle this efficiently, we'll precompute the prefix sums of the original array
    # Then, for any rotation, we can compute the current array's prefix sums using the original array's prefix sums
    
    # Precompute prefix sums of the original array
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + A[i]
    
    # Precompute the maximum length of consecutive 1s in the original array
    # This is for the case when there are no rotations
    max_len = 0
    current = 0
    for num in A:
        if num == 1:
            current += 1
            max_len = max(max_len, current)
        else:
            current = 0
    
    # Now handle the queries
    rot = 0  # current rotation offset
    for c in S:
        if c == '!':
            # Right shift the array
            rot = (rot + 1) % N
        else:
            # Query for the maximum length of consecutive 1s with length <= K
            # We need to find the maximum length of consecutive 1s in the current array
            # The current array is A[rot], A[rot+1], ..., A[N-1], A[0], A[1], ..., A[rot-1]
            # To find the maximum length of consecutive 1s, we can use the prefix sums
            # We can compute the maximum length of consecutive 1s in the current array
            # by checking all possible windows of size up to K
            # But since N is up to 1e5 and Q is up to 3e5, we need an efficient way
            # We can precompute for all possible rotations the maximum length of consecutive 1s
            # However, that would be O(N^2), which is not feasible
            # So instead, we can use a sliding window approach for each query
            # But that would be O(Q*N), which is also not feasible
            # So we need a better approach
            # Let's precompute for all possible rotations the maximum length of consecutive 1s
            # and the positions of the consecutive 1s
            # But again, that's not feasible for N up to 1e5
            # So we need a way to compute the maximum length of consecutive 1s in the current array
            # efficiently
            
            # Let's compute the maximum length of consecutive 1s in the current array
            # The current array is A[rot], A[rot+1], ..., A[N-1], A[0], A[1], ..., A[rot-1]
            # So we can treat this as a circular array
            # We can compute the maximum length of consecutive 1s in a circular array
            # The maximum length of consecutive 1s in a circular array is either the maximum in the linear array or the total number of 1s if the array is all 1s
            # So we can compute the maximum length of consecutive 1s in the current array
            # as follows:
            # 1. Compute the maximum length of consecutive 1s in the linear array
            # 2. Compute the total number of 1s in the array
            # 3. If the total number of 1s is equal to N, then the maximum is N
            # 4. Otherwise, the maximum is the maximum of the linear array and the total number of 1s if the array is all 1s
            # But this is not correct
            # We need to find the maximum length of consecutive 1s in the circular array
            # We can do this by checking the maximum length of consecutive 1s in the linear array and the maximum length of consecutive 1s that wraps around the end and the beginning
            # So let's compute the maximum length of consecutive 1s in the current array
            # by considering the linear array and the circular part
            
            # Compute the maximum length of consecutive 1s in the current array
            max_len_current = 0
            current = 0
            for i in range(N):
                if A[(rot + i) % N] == 1:
                    current += 1
                    max_len_current = max(max_len_current, current)
                else:
                    current = 0
            # Now check if there is a wrap-around sequence
            # Check if the first and last elements are 1
            if A[rot] == 1 and A[(rot + N - 1) % N] == 1:
                # Check if the total number of 1s is equal to N
                total_ones = 0
                for i in range(N):
                    if A[i] == 1:
                        total_ones += 1
                if total_ones == N:
                    max_len_current = N
                else:
                    # Check the length of the sequence from the end to the beginning
                    current = 0
                    for i in range(N-1, -1, -1):
                        if A[i] == 1:
                            current += 1
                            max_len_current = max(max_len_current, current)
                        else:
                            break
            # Now, the maximum length of consecutive 1s is max_len_current
            # But we need to find the maximum length that is <= K
            # So the answer is min(max_len_current, K)
            print(min(max_len_current, K))
    
if __name__ == '__main__':
    solve()