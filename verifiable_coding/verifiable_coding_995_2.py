import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    A = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    
    # We can only start from the leftmost or rightmost room
    # So we consider two cases: starting from left or starting from right
    
    # Case 1: start from left
    left = []
    for i in range(n):
        left.append(A[i])
        if i > 0:
            left[i] += left[i-1]
    
    # Case 2: start from right
    right = [0] * n
    right[-1] = A[-1]
    for i in range(n-2, -1, -1):
        right[i] = A[i] + right[i+1]
    
    # Now, we need to choose the maximum sum of k elements from the left or right arrays
    # But we can only take k elements from one side, not both
    
    # We can take up to k elements from the left or right
    # We need to find the maximum sum of k elements from the left or right
    
    # For the left array, we can take the top k elements
    # Similarly for the right array
    
    # To find the top k elements, we can use a max heap
    import heapq
    
    # Get top k elements from left
    left_top = heapq.nlargest(k, left)
    left_sum = sum(left_top)
    
    # Get top k elements from right
    right_top = heapq.nlargest(k, right)
    right_sum = sum(right_top)
    
    print(max(left_sum, right_sum))
    
if __name__ == '__main__':
    solve()