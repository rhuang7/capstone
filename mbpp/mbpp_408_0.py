def check(candidate):
    assert candidate([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert candidate([1,3,7],[2,4,6],1)==[[1, 2]]
    assert candidate([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]


def find_k_pairs(arr1, arr2, k):
    import heapq

    # Create a min-heap to store pairs (sum, index1, index2)
    heap = []
    # Initialize the heap with the first element of each array
    for i in range(len(arr1)):
        heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))
    
    # Use a set to keep track of visited indices in arr2
    visited = set()
    result = []

    # Extract k pairs from the heap
    for _ in range(k):
        if not heap:
            break  # Not enough pairs
        sum_val, i, j = heapq.heappop(heap)
        result.append((arr1[i], arr2[j]))
        # Push the next element from arr2 for the same index in arr1
        if j + 1 < len(arr2) and (i, j + 1) not in visited:
            visited.add((i, j + 1))
            heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
    
    return result

check(find_k_pairs)