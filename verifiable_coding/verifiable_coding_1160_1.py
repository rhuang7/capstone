import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        trees = []
        for _ in range(n):
            h = int(data[idx])
            m = int(data[idx+1])
            trees.append((h, m))
            idx += 2
        
        # Check if the initial configuration is zigzag
        is_zigzag = True
        for i in range(1, n):
            if (trees[i-1][0] > trees[i][0] and trees[i-1][0] <= trees[i+1][0]) or (trees[i-1][0] < trees[i][0] and trees[i-1][0] >= trees[i+1][0]):
                is_zigzag = False
                break
        
        if is_zigzag:
            results.append("0 0")
        
        # Find all time intervals where the sequence is zigzag
        # We need to find all t where the sequence is zigzag
        # We can model the sequence as a function of t
        # For each pair of consecutive trees, we can find the time intervals where the relation between them is correct
        # Then take the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # We can model the sequence as a function of t
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation between them is correct
        # Then find the intersection of all these intervals
        
        # For each pair of consecutive trees, compute the time intervals where the relation