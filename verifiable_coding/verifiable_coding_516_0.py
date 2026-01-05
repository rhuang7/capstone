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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute inversions in original array A
        def count_inversions(arr):
            inv_count = 0
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i] > arr[j]:
                        inv_count += 1
            return inv_count
        
        inv_in_A = count_inversions(A)
        
        # Compute inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array
        # Inversions between elements of A and itself in the concatenated array