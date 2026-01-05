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
        w.sort()
        
        # To maximize happiness, we need to assign the largest elements as max and the smallest as min
        # For each friend, the max is the largest element in their group, the min is the smallest
        # So, we take the largest (k) elements as max and the smallest (k) elements as min
        # But since each friend gets exactly w_i elements, we need to assign the largest (k) elements as max and the smallest (k) elements as min
        
        # The total happiness is sum of (max + min) for each friend
        # So, we take the largest k elements as max and the smallest k elements as min
        # But we need to assign them in a way that each friend gets exactly w_i elements
        
        # Sort the array
        a.sort()
        
        # Take the largest k elements as max
        max_elements = a[-k:]
        # Take the smallest k elements as min
        min_elements = a[:k]
        
        # Now, we need to assign these elements to friends in a way that each friend gets exactly w_i elements
        # The max elements are sorted in ascending order, so we take the largest ones first
        # The min elements are sorted in ascending order, so we take the smallest ones first
        
        # The total happiness is sum of (max + min) for each friend
        # So, we take the largest k elements as max and the smallest k elements as min
        # Then, for each friend, we take the largest available max and the smallest available min
        
        # Sort the max elements in ascending order (so we can take the largest ones first)
        max_elements.sort()
        # Sort the min elements in ascending order (so we can take the smallest ones first)
        min_elements.sort()
        
        # Now, assign the max and min elements to friends
        # We need to take the largest max and smallest min for each friend
        # So, we take the largest max and smallest min for each friend
        
        # The total happiness is sum of (max + min) for each friend
        total_happiness = 0
        max_ptr = len(max_elements) - 1
        min_ptr = 0
        for i in range(k):
            total_happiness += (max_elements[max_ptr] + min_elements[min_ptr])
            max_ptr -= 1
            min_ptr += 1
        
        results.append(str(total_happiness))
    
    print('\n'.join(results))