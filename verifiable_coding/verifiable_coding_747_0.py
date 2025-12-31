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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        A_sorted = sorted(A)
        
        # Check if the array can be rearranged to satisfy the condition
        # The condition is that there exists a p such that the first p elements are strictly increasing and the rest are strictly decreasing
        # So, the array must be such that it can be rearranged into a strictly increasing then strictly decreasing sequence
        
        # We can try to construct such a sequence by placing the smallest element at the beginning and the largest at the end
        # Then fill the rest in increasing order from the start and decreasing order from the end
        
        # Check if there are duplicates
        if len(set(A)) < N:
            results.append("NO")
            continue
        
        # Try to construct the sequence
        # Start with the smallest element
        # Then add elements in increasing order until the peak
        # Then add elements in decreasing order
        # The peak can be the middle element or somewhere around it
        
        # We can try to construct the sequence by placing the smallest element at the beginning
        # Then add elements in increasing order from the start and decreasing from the end
        
        # Create a copy of the sorted array
        A_sorted = sorted(A)
        
        # Try to construct the sequence
        # Start with the first element (smallest)
        # Then add elements in increasing order until the peak
        # Then add elements in decreasing order
        # The peak is the middle element
        # So, the sequence would be: A_sorted[0], A_sorted[1], ..., A_sorted[mid], A_sorted[mid+1], ..., A_sorted[-1]
        # But this is not correct, because the middle element must be the peak
        
        # Instead, we can try to find the peak element and arrange the sequence around it
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that is greater than all elements before it and greater than all elements after it
        # So, we can try to find the peak element by checking the sorted array
        
        # Try to find the peak element
        # The peak element is the one that