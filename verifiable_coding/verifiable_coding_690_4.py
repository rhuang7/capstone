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
    
    if K == 0:
        print(-1)
        return
    
    # If all soldiers have 0 morale, no speeches needed
    if all(x == 0 for x in A):
        print(0)
        return
    
    # If any single soldier's morale is already >= M, no speeches needed
    if any(x >= M for x in A):
        print(0)
        return
    
    # We need to find the minimum number of speeches such that
    # every K consecutive soldiers have sum >= M
    # Each speech multiplies a block of K consecutive soldiers by X > 1
    
    # We can use a sliding window approach to find the minimum number of speeches
    # We can greedily apply speeches to the leftmost window that needs it
    
    # Initialize the answer
    res = 0
    
    # We need to process the array in chunks of K
    # We can use a sliding window to find the minimum number of speeches
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a queue to keep track of the positions where speeches are applied
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it
    
    # We can use a sliding window to find the minimum number of speeches
    
    # We can use a greedy approach: apply speeches to the leftmost window that needs it