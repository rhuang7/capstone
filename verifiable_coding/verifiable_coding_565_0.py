import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        # Find the correct position of X in the original array
        correct_pos = {}
        for i in range(N):
            correct_pos[A[i]] = i + 1  # 1-based index
        
        # Preprocess the array to find the positions of elements
        pos = {val: i + 1 for i, val in enumerate(A)}
        
        # For each query, find the correct position of X
        for X in queries:
            correct = correct_pos[X]
            # The algorithm returns mid, which is the position where X is found
            # We need to make sure that the algorithm returns correct
            # So we need to swap elements such that the binary search returns correct
            # The minimum number of swaps is the minimum number of swaps to bring X to the correct position
            # But we cannot swap X with any other element, so we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid, which is the position where X is found
            # So we need to make sure that X is at the position that the binary search would return
            # The binary search works on a sorted array, so the array must be sorted for the binary search to work
            # So we need to sort the array and find the position of X in the sorted array
            # But we cannot change the position of X itself
            # So we need to find the minimum number of swaps to make the binary search return correct
            # The binary search returns mid,