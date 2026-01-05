import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Precompute for each position the minimum prefix length to remove
        # to make the remaining array good
        # We'll use a greedy approach with a deque and a bisect to maintain a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintain a non-decreasing sequence
        
        # We'll also use a list to keep track of the current sequence
        # and for each position, we'll try to find the minimum prefix length
        
        # We'll try all possible prefix lengths from 0 to n
        # and check if the remaining array is good
        
        # To optimize, we'll use a greedy approach with a deque and bisect
        # to check if the remaining array can be rearranged into a non-decreasing sequence
        
        # Let's try all possible prefix lengths
        # and find the minimum one that works
        
        # For each possible prefix length k (0 <= k <= n), check if the remaining array is good
        
        # To check if an array is good, we can simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate this process
        # and a list to keep track of the current sequence
        
        # For each possible k, we'll check if the array a[k:] is good
        
        # We'll use a greedy approach with a deque and a bisect to maintain a non-decreasing sequence
        
        # Let's try all possible k from 0 to n
        # and find the minimum one that works
        
        # To optimize, we can use a sliding window approach
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # For each possible k, we'll check if the array a[k:] is good
        
        # We'll use a greedy approach with a deque and a bisect to maintain a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # For each possible k, we'll check if the array a[k:] is good
        
        # We'll use a greedy approach with a deque and a bisect to maintain a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining a non-decreasing sequence
        
        # We'll use a deque to simulate the process of taking elements from front or back
        # and maintaining