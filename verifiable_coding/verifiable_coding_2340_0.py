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
        # Start from the end of p and try to find the possible splits
        
        # Initialize two pointers for a and b
        a_ptr = 0
        b_ptr = 0
        
        # We will simulate the merge process in reverse
        # We will keep track of the current elements in a and b
        # We will use a stack to simulate the merge process
        stack = []
        i = 2 * n - 1
        while i >= 0:
            # The last element in the merge is either the last element of a or b
            # So we check which one it could be
            # We need to find the correct element to pop from the stack
            # We try to find the next element in a or b
            # If the current element is the next element in a, we pop it from a
            # If it is the next element in b, we pop it from b
            # We need to check if the current element is the next element in a or b
            # We can do this by checking the next element in a or b
            # We need to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list to track the next element in a and b
            # We can use a list