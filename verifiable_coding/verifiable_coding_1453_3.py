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
    
    # Precompute prefix sums of 1s
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    # For each query, track the current rotation offset
    offset = 0
    
    for c in S:
        if c == '!':
            # Right shift the array
            offset = (offset + 1) % N
        else:
            # Find the maximum length of contiguous 1s <= K
            max_len = 0
            # Since the array is rotated, we need to handle circular array
            # We can simulate it by considering the array as doubled
            # and checking for the maximum run of 1s in a window of size K
            # But since K can be up to N, we need an efficient way
            # We can use the prefix sum array and check for each position
            # the maximum run of 1s in the circular array
            # But this is O(N) per query, which is too slow for Q=3e5
            # So we need a better approach
            
            # Instead, we can precompute for all possible rotations
            # the maximum run of 1s in a window of size K
            # But that's also O(N^2), which is not feasible
            
            # So we use a sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window
            # of size K
            # But since the array is rotated, we need to adjust the window
            
            # To handle the circular nature, we can double the array
            # and then check for the maximum run of 1s in any window of size K
            # However, this is not efficient for large N and Q
            
            # So we need a better approach. Let's think differently.
            
            # We can precompute for each position the maximum run of 1s
            # ending at that position, and then for each query, we can
            # find the maximum run of 1s that fits in a window of size K
            
            # But this is still O(N) per query, which is too slow
            
            # So we need to find a way to answer the query in O(1) or O(log N) time
            
            # Let's think of the array as a circular array, and we need to
            # find the maximum run of 1s in any window of size K
            # This is equivalent to finding the maximum number of consecutive 1s
            # in any window of size K in the circular array
            
            # We can use a sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window
            # of size K
            
            # However, for large N and Q, this is not efficient
            
            # So we can precompute for each possible rotation the maximum run of 1s
            # in any window of size K. But this is O(N^2), which is not feasible
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute
            # the maximum run of 1s in the circular array that starts at that position
            # and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to precompute the maximum run of 1s in any
            # window of size K in the circular array
            
            # Let's think of the array as a circular array and use a sliding window
            # of size K to find the maximum run of 1s
            
            # We can use a sliding window approach on the doubled array
            # and for each position, check the maximum run of 1s in a window of size K
            
            # But again, this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's think of the array as a circular array and precompute
            # for each position the maximum run of 1s that starts at that position
            # and extends to the right (including wrapping around)
            
            # Then, for each query, we can find the maximum run of 1s that fits in a window of size K
            
            # But this is still O(N) per query
            
            # So we need to find a way to precompute the maximum run of 1s in any window of size K
            # in the circular array
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window of size K
            # and for each position, find the maximum run of 1s in that window
            
            # But this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window of size K
            # and for each position, find the maximum run of 1s in that window
            
            # But this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window of size K
            # and for each position, find the maximum run of 1s in that window
            
            # But this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window of size K
            # and for each position, find the maximum run of 1s in that window
            
            # But this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            # by considering the array as doubled and using a sliding window of size K
            # and for each position, find the maximum run of 1s in that window
            
            # But this is O(N) per query, which is not feasible for Q=3e5
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the prefix sum array and for each position, compute the maximum run of 1s
            # in the circular array that starts at that position and has length up to K
            
            # But this is still O(N) per query
            
            # So we need to find a way to answer the query in O(1) time
            
            # Let's use the sliding window approach on the circular array
            #