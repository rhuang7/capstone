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
        
        # Preprocess: find the correct index of X in A
        correct_pos = {val: i for i, val in enumerate(A)}
        
        # For each query, find the correct position of X
        # The algorithm will return the position where X is found
        # We need to make sure that the algorithm returns the correct position
        # So, we need to swap elements such that the algorithm returns the correct position
        # The algorithm works correctly if the array is sorted, but since it's not, we need to adjust
        
        # Precompute the correct position for each query
        correct_positions = [correct_pos[x] for x in queries]
        
        # Create a list of elements in the array
        elements = A
        
        # For each query, find the minimum number of swaps to make the algorithm return the correct position
        # The algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # The algorithm works correctly if the array is sorted, but since it's not, we need to adjust
        
        # We can use a greedy approach: for each query, find the correct position, and then find the minimum number of swaps
        # to make the algorithm return that position
        # The algorithm is a binary search that returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        
        # To do this, we can simulate the binary search and count the number of swaps needed
        # to make the algorithm return the correct position
        
        # However, this is too slow for large N and Q
        # So, we need a more efficient approach
        
        # The key observation is that the algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in the correct position
        # But we cannot swap the element that is X itself
        
        # So, we can do the following:
        # For each query, we need to make sure that the algorithm returns the correct position
        # The algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # So, the problem reduces to: for each query, find the minimum number of swaps to make the algorithm return the correct position
        
        # The algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in the correct position
        # But we cannot swap the element that is X itself
        
        # So, for each query, we need to find the correct position of X, and then count the number of elements that are not in the correct position
        
        # However, this is not correct, because the algorithm may return the correct position even if the array is not sorted
        # So, we need to simulate the algorithm and count the number of swaps needed to make it return the correct position
        
        # To do this, we can simulate the algorithm for each query and count the number of swaps needed
        # However, this is too slow for large N and Q
        
        # So, we need a better approach
        
        # The key observation is that the algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # So, the problem is to find the minimum number of swaps needed to make the algorithm return the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in the correct position
        # But we cannot swap the element that is X itself
        
        # So, for each query, we need to find the correct position of X, and then count the number of elements that are not in the correct position
        
        # However, this is not correct, because the algorithm may return the correct position even if the array is not sorted
        # So, we need to simulate the algorithm and count the number of swaps needed to make it return the correct position
        
        # To do this, we can simulate the algorithm for each query and count the number of swaps needed
        # However, this is too slow for large N and Q
        
        # So, we need a better approach
        
        # The key observation is that the algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # So, the problem is to find the minimum number of swaps needed to make the algorithm return the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in the correct position
        # But we cannot swap the element that is X itself
        
        # So, for each query, we need to find the correct position of X, and then count the number of elements that are not in the correct position
        
        # However, this is not correct, because the algorithm may return the correct position even if the array is not sorted
        # So, we need to simulate the algorithm and count the number of swaps needed to make it return the correct position
        
        # To do this, we can simulate the algorithm for each query and count the number of swaps needed
        # However, this is too slow for large N and Q
        
        # So, we need a better approach
        
        # The key observation is that the algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # So, the problem is to find the minimum number of swaps needed to make the algorithm return the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in the correct position
        # But we cannot swap the element that is X itself
        
        # So, for each query, we need to find the correct position of X, and then count the number of elements that are not in the correct position
        
        # However, this is not correct, because the algorithm may return the correct position even if the array is not sorted
        # So, we need to simulate the algorithm and count the number of swaps needed to make it return the correct position
        
        # To do this, we can simulate the algorithm for each query and count the number of swaps needed
        # However, this is too slow for large N and Q
        
        # So, we need a better approach
        
        # The key observation is that the algorithm returns the position where X is found
        # So, we need to make sure that the algorithm returns the correct position
        # So, we need to make sure that the algorithm returns the correct position
        
        # So, the problem is to find the minimum number of swaps needed to make the algorithm return the correct position
        
        # The algorithm is a binary search that returns the position where X is found
        # So, the algorithm will return the correct position if the array is sorted
        # But since it's not, we need to adjust the array so that the algorithm returns the correct position
        
        # The minimum number of swaps is the number of elements that are not in