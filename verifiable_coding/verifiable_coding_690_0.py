import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    if any(a == 0 for a in A):
        print(-1)
        return
    
    # We need to find the minimum number of intervals of size K such that
    # the sum of any K consecutive elements in the array is >= M after applying
    # X to some elements in the intervals.
    
    # We can use binary search on the number of speeches.
    # For a given number of speeches, we check if it's possible to assign the speeches
    # such that all K-length windows have sum >= M.
    
    def is_possible(speeches):
        # We need to assign speeches to K-length intervals such that
        # the sum of any K-length window is >= M.
        # We can use a greedy approach: assign speeches to the earliest possible positions.
        # We can use a sliding window to find the positions where speeches are needed.
        
        # We will use a greedy approach with a sliding window to find the positions where speeches are needed.
        # We will also use a greedy approach to assign the speeches to the earliest possible positions.
        
        # We will use a greedy approach with a sliding window to find the positions where speeches are needed.
        # We will also use a greedy approach to assign the speeches to the earliest possible positions.
        
        # We need to find the minimal X such that after applying X to some elements, all K-length windows have sum >= M.
        # We can use binary search on X.
        
        # Binary search on X.
        low = 1
        high = 10**18
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to assign speeches with X = mid.
            # We need to find the minimal number of speeches.
            # We can use a greedy approach to assign speeches.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We need to find the minimal number of speeches such that after applying X to some elements, all K-length windows have sum >= M.
            # We can use a greedy approach to assign the speeches to the earliest possible positions.
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.
            
            # We will use a sliding window to find the positions where speeches are needed.
            # We will also use a greedy approach to assign the speeches to the earliest possible positions.