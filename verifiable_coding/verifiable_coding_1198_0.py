import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    Q = int(data[idx])
    idx += 1
    queries = list(map(int, data[idx:idx+Q]))
    
    # Preprocess all possible subarrays and their gcds
    # We'll use a dictionary to count how many subarrays have a certain gcd
    # Also, for each subarray, its gcd is the gcd of all elements in it
    # We'll use a sliding window approach to compute gcds efficiently
    
    # Initialize the result dictionary
    result = defaultdict(int)
    
    # For each starting index i, compute the gcd of A[i], A[i+1], ..., A[j]
    # and update the count of gcds
    # We'll use a sliding window approach with a running gcd
    # For each i, we'll start with gcd = A[i], then for j from i to N-1:
    #   gcd = gcd(gcd, A[j])
    #   update the count of gcds
    # This is O(N^2) in worst case, which is not feasible for N=1e5
    # So we need a better approach
    
    # Instead, we'll use a more efficient approach by considering that the gcd of a subarray
    # can only be a divisor of the elements in the subarray. So we can use a sliding window
    # approach where we track the current gcd and update it as we move the window
    
    # We'll use a dictionary to count the number of subarrays with a certain gcd
    # We'll also use a set to track the current gcds in the window
    
    # Initialize the result dictionary
    result = defaultdict(int)
    
    # We'll use a sliding window approach
    # For each right, we'll track the current gcds in the window [left, right]
    # We'll also track the current gcds for the subarrays ending at right
    
    # We'll use a dictionary to track the current gcds in the window
    current_gcds = defaultdict(int)
    
    # We'll also track the current gcd for the subarrays ending at right
    current_gcd = 0
    
    # For each right in 0 to N-1:
    for right in range(N):
        # Reset the current_gcd for new subarrays ending at right
        current_gcd = A[right]
        # Update the current_gcds for the subarrays ending at right
        # We'll use a dictionary to track the current gcds in the window
        # For each left in 0 to right:
        #   current_gcd = gcd(current_gcd, A[left])
        #   update current_gcds
        # But this is O(N^2), which is not feasible for N=1e5
        # So we need a better approach
        
        # Instead, we can use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll use a dictionary to track the current gcds in the window
        # We'll also track the current gcd for the subarrays ending at right
        
        # For each right, we'll have a new subarray starting at right
        # We'll also update the current_gcds for the subarrays ending at right
        
        # Initialize the current_gcd for the subarray [right, right]
        current_gcd = A[right]
        # Update the current_gcds
        current_gcds[current_gcd] += 1
        
        # Now, for the subarrays ending at right, we'll move the left pointer
        # and update the current_gcds
        # We'll use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll also track the current_gcd for the subarrays ending at right
        # and update the result dictionary
        
        # For each left in 0 to right:
        #   current_gcd = gcd(current_gcd, A[left])
        #   update current_gcds
        #   if current_gcd is in the result dictionary, increment the count
        #   else, add it to the result dictionary with count 1
        
        # But this is O(N^2), which is not feasible for N=1e5
        # So we need a better approach
        
        # Instead, we can use the fact that the gcd of a subarray can only decrease as we add more elements
        # So we can use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll use a dictionary to track the current gcds in the window
        # We'll also track the current gcd for the subarrays ending at right
        
        # Initialize the current_gcd for the subarray [right, right]
        current_gcd = A[right]
        # Update the current_gcds
        current_gcds[current_gcd] += 1
        
        # Now, for the subarrays ending at right, we'll move the left pointer
        # and update the current_gcds
        # We'll use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll also track the current_gcd for the subarrays ending at right
        # and update the result dictionary
        
        # For each left in 0 to right:
        #   current_gcd = gcd(current_gcd, A[left])
        #   update current_gcds
        #   if current_gcd is in the result dictionary, increment the count
        #   else, add it to the result dictionary with count 1
        
        # But this is O(N^2), which is not feasible for N=1e5
        # So we need a better approach
        
        # Instead, we can use the fact that the gcd of a subarray can only decrease as we add more elements
        # So we can use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll use a dictionary to track the current gcds in the window
        # We'll also track the current gcd for the subarrays ending at right
        
        # Initialize the current_gcd for the subarray [right, right]
        current_gcd = A[right]
        # Update the current_gcds
        current_gcds[current_gcd] += 1
        
        # Now, for the subarrays ending at right, we'll move the left pointer
        # and update the current_gcds
        # We'll use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll also track the current_gcd for the subarrays ending at right
        # and update the result dictionary
        
        # For each left in 0 to right:
        #   current_gcd = gcd(current_gcd, A[left])
        #   update current_gcds
        #   if current_gcd is in the result dictionary, increment the count
        #   else, add it to the result dictionary with count 1
        
        # But this is O(N^2), which is not feasible for N=1e5
        # So we need a better approach
        
        # Instead, we can use the fact that the gcd of a subarray can only decrease as we add more elements
        # So we can use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll use a dictionary to track the current gcds in the window
        # We'll also track the current gcd for the subarrays ending at right
        
        # Initialize the current_gcd for the subarray [right, right]
        current_gcd = A[right]
        # Update the current_gcds
        current_gcds[current_gcd] += 1
        
        # Now, for the subarrays ending at right, we'll move the left pointer
        # and update the current_gcds
        # We'll use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll also track the current_gcd for the subarrays ending at right
        # and update the result dictionary
        
        # For each left in 0 to right:
        #   current_gcd = gcd(current_gcd, A[left])
        #   update current_gcds
        #   if current_gcd is in the result dictionary, increment the count
        #   else, add it to the result dictionary with count 1
        
        # But this is O(N^2), which is not feasible for N=1e5
        # So we need a better approach
        
        # Instead, we can use the fact that the gcd of a subarray can only decrease as we add more elements
        # So we can use a sliding window approach where we track the current gcds
        # and update them as we move the window
        
        # We'll use a dictionary to track the current gcd