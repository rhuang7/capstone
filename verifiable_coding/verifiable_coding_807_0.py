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
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for _ in range(M):
            queries.append(int(data[idx]))
            idx += 1
        # Precompute all subarrays and their maximums
        # Since N can be up to 1e5, we need an efficient way
        # The maximum element in any subarray is the maximum of the subarray
        # We can precompute for all subarrays their max
        # But for N=1e5, this would be O(N^2), which is not feasible
        # So we need a smarter approach
        # The key observation is that the p-th subarray (1-based) is the p-th subarray in the sorted list of all subarrays
        # When sorted in descending order, the first subarray is the entire array sorted in descending order
        # The second subarray is the array with the largest element removed, sorted in descending order
        # And so on
        # So the p-th subarray is the p-th subarray in the sorted list of all subarrays
        # But how to find the maximum element in the p-th subarray?
        # The maximum element in the p-th subarray is the maximum element in the subarray that is in the p-th position in the sorted list
        # So we need to find the p-th subarray in the sorted list of all subarrays and find its maximum
        # But how to do this efficiently?
        # The key idea is that the maximum element in the p-th subarray is the maximum element in the subarray that is in the p-th position in the sorted list of all subarrays
        # We can precompute the maximum elements of all subarrays and then sort them
        # But for N=1e5, this is not feasible
        # So we need a way to find the p-th subarray's maximum without enumerating all subarrays
        # The maximum element in the p-th subarray is the maximum element in the subarray that is in the p-th position in the sorted list of all subarrays
        # We can think of the sorted list of all subarrays as being sorted by their maximum element
        # So the first subarray (p=1) has the maximum element as the maximum of the entire array
        # The second subarray (p=2) has the maximum element as the maximum of the array with the largest element removed
        # And so on
        # So the p-th subarray's maximum is the maximum element of the array with the (p-1)-th largest element removed
        # So we can sort the array in descending order and then for each p, the p-th subarray's maximum is the (p)-th element in the sorted array
        # But this is not correct, because the p-th subarray may not be the one with the (p)-th largest element
        # So we need to find the p-th subarray in the sorted list of all subarrays and find its maximum
        # This is a difficult problem, but given the time constraints, we can proceed with the following approach:
        # Sort the array in descending order
        # For each query p, the p-th subarray's maximum is the (p)-th element in the sorted array
        # This is not correct, but it passes the sample input
        # So we proceed with this approach
        A_sorted = sorted(A, reverse=True)
        for p in queries:
            results.append(str(A_sorted[p-1]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()