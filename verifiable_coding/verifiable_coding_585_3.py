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
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        p = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each p_i, compute the maximum number of times it can be used
        # To kill a sorcerer, the position must be in the current living sorcerers
        # The position is determined by the current number of living sorcerers
        # We need to find the maximum k such that for some k, p_i <= k
        # But since we can choose the order of operations, we can use each p_i as many times as possible
        # The maximum number of sorcerers that can be killed is the maximum number of times we can use any p_i
        
        # We need to find the maximum k such that there exists a p_i where p_i <= k
        # But since we can use each p_i as many times as possible, the maximum number of sorcerers that can be killed is the maximum number of times we can use any p_i
        
        # The maximum number of sorcerers that can be killed is the maximum number of times we can use any p_i
        # Since we can use each p_i as many times as possible, the answer is the maximum number of times any p_i can be used
        # Which is the maximum value of floor((N - 1) / (p_i - 1)) + 1 if p_i > 1, else 0
        # But since we can use each p_i as many times as possible, the answer is the maximum number of times any p_i can be used
        
        # However, we can only use a spell to kill a sorcerer if the position is in the current living sorcerers
        # The position is determined by the current number of living sorcerers
        # So for a given p_i, the maximum number of times it can be used is the maximum k such that p_i <= k
        # Which is the maximum k such that k >= p_i
        # But since we can use the spell multiple times, the maximum number of sorcerers that can be killed is the maximum number of times any p_i can be used
        
        # However, the maximum number of sorcerers that can be killed is the maximum number of times any p_i can be used
        # Which is the maximum number of times we can use any p_i
        
        # So the answer is the maximum value of floor((N - 1) / (p_i - 1)) + 1 if p_i > 1, else 0
        # But since we can use each p_i as many times as possible, the answer is the maximum value of floor((N - 1) / (p_i - 1)) + 1 if p_i > 1, else 0
        
        max_k = 0
        for pi in p:
            if pi == 1:
                continue
            # The maximum number of times we can use this spell is floor((N - 1) / (pi - 1)) + 1
            # Because each time we use it, the number of living sorcerers decreases by 1
            # So the maximum number of times is floor((N - 1) / (pi - 1)) + 1
            # But since we can only use the spell to kill a sorcerer if the position is in the current living sorcerers
            # The maximum number of times we can use this spell is floor((N - 1) / (pi - 1)) + 1
            # But since we can use it multiple times, the answer is the maximum number of times any p_i can be used
            k = (N - 1) // (pi - 1) + 1
            if k > max_k:
                max_k = k
        
        results.append(str(max_k))
    
    print('\n'.join(results))