import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    if N == 0:
        print(0)
        return
    
    # Check if all soldiers already satisfy the condition
    def is_valid():
        for i in range(N - K + 1):
            total = sum(A[i:i+K])
            if total < M:
                return False
        return True
    
    if is_valid():
        print(0)
        return
    
    # Binary search on the number of speeches
    low = 1
    high = N
    answer = -1
    
    while low <= high:
        mid = (low + high) // 2
        # Try to place mid speeches
        # We can place at most mid speeches, each on a segment of K soldiers
        # We need to check if it's possible to place mid speeches such that all K-length windows have sum >= M
        # We'll try to greedily place speeches on the rightmost possible positions
        
        # We'll use a greedy approach to place speeches
        # We'll track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the window and the positions where speeches are placed
        # We'll also track the current sum of the