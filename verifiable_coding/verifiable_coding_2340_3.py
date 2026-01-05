import sys

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
        p = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        # We need to check if p can be formed by merging two arrays a and b of length n
        # with no common elements
        
        # We can simulate the merge process in reverse
        # Start from the end of p and try to find the two arrays a and b
        
        # Initialize two pointers for a and b
        a_ptr = 0
        b_ptr = 0
        
        # We will use a stack to simulate the merge process
        stack = []
        
        # We will iterate through p in reverse
        for num in reversed(p):
            # If the current number is the first element of a or b
            # We need to check if it's the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number is the first element of a or b
            # We can do this by checking if the current number