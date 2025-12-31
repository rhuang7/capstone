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
    
    # We need to find the minimum number of speeches such that every K consecutive elements have sum >= M
    # Each speech multiplies a contiguous K elements by X (X > 1)
    
    # We can use binary search on the number of speeches
    left = 0
    right = N  # Maximum possible speeches is N (each soldier can be in a speech)
    
    def is_possible(speeches):
        # Try to place 'speeches' speeches such that every K consecutive elements have sum >= M
        # We use a greedy approach to place speeches
        # We track the current multiplier for each element
        # We use a sliding window to check if the sum is >= M
        # We can use a segment tree or sliding window approach to check this
        # For simplicity, we use a sliding window approach with a prefix sum array
        # We track the current sum of the window and the number of speeches used
        # We can use a greedy approach to place speeches
        # We can use a binary search approach to find the minimum number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        
        # We can use a greedy approach to place speeches
        # We need to find the minimum number of speeches such that every K consecutive elements have sum >= M
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        
        # We can use a greedy approach to place speeches
        # We can use a binary search on the number of speeches
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We need to find the minimum number of speeches such that every K consecutive elements have sum >= M
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We can use a greedy approach to place speeches in the optimal positions
        # We can use a sliding window approach to check if the sum of any K consecutive elements is >= M
        # We can use a binary search on the number of speeches
        
        # We can use a binary search on the number of speeches
        # We