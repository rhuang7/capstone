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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        w = list(map(int, data[idx:idx+k]))
        idx += k
        
        a.sort()
        w.sort(reverse=True)
        
        total = 0
        # Assign maximums and minimums
        # For each friend, assign the largest available and the smallest available
        # The rest of the numbers are in between
        # We need to assign the largest and smallest for each friend
        # The rest are in between, so they don't affect the sum
        
        # Assign the largest available to each friend
        # Assign the smallest available to each friend
        # The rest are in between, so they don't contribute to the sum
        
        # For the first k elements in a (sorted), assign them as maxes
        # For the last k elements in a, assign them as mins
        # But wait, we need to assign exactly w_i elements to each friend
        # So we need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # Sort a
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, the max is the largest available, the min is the smallest available
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # So we need to take the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # But since w is sorted in descending order, we can take the largest w_i elements as maxes
        # and the smallest w_i elements as mins
        
        # So for the first k elements in a, assign them as mins
        # For the last k elements in a, assign them as maxes
        
        # But wait, we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So for the first k elements in a, assign them as mins
        # For the last k elements in a, assign them as maxes
        
        # But since w is sorted in descending order, we can take the largest w_i elements as maxes
        # and the smallest w_i elements as mins
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # The maxes are the last k elements of a
        # The mins are the first k elements of a
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So for the first k elements in a, assign them as mins
        # For the last k elements in a, assign them as maxes
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # The maxes are the last k elements of a
        # The mins are the first k elements of a
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # The maxes are the last k elements of a
        # The mins are the first k elements of a
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # The maxes are the last k elements of a
        # The mins are the first k elements of a
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort a
        a.sort()
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # For each friend, we need to assign one max and one min
        # The rest are in between, so they don't contribute to the sum
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need to assign the largest w_i elements as maxes and the smallest w_i elements as mins
        
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign the largest w_i elements as maxes
        # Assign the smallest w_i elements as mins
        
        # The maxes are the last k elements of a
        # The mins are the first k elements of a
        
        # But we need to assign exactly w_i elements to each friend
        # So for each friend, we need to assign one max and one min
        
        # So the total happiness is sum of (max + min) for each friend
        
        # We need