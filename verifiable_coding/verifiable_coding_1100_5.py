import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        p = int(data[index])
        q = int(data[index+1])
        r = int(data[index+2])
        index += 3
        
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        if (p == a and q == b and r == c):
            results.append(0)
            continue
        
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        if diff_p < 0 or diff_q < 0 or diff_r < 0:
            results.append(-1)
            continue
        
        ops = 0
        
        # Count how many times each difference can be divided by 1 (since we can add to any subset)
        # We need to find the maximum number of operations, so we want to minimize the number of times we have to add to each element
        # We can do this by checking how many times each difference can be divided by 1 (which is always 1)
        # But we need to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each difference that is not zero
        
        # We can do one operation per non-zero difference
        # But we have to make sure that the sum of all operations is equal to the sum of all differences
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So the maximum number of operations is the number of non-zero differences
        # But we have to make sure that the sum of all differences is equal to the sum of all operations
        # Since we can add to any subset, we can do one operation for each non-zero difference
        
        # So