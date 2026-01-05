import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_star = 0
        freq = defaultdict(int)
        max_val = 0
        
        for num in A:
            max_val = max(max_val, num)
        
        # Use a frequency array to count multiples
        freq_arr = [0] * (max_val + 1)
        
        for num in A:
            # Count how many numbers divisible by num have been seen so far
            count = 0
            for i in range(num, max_val + 1, num):
                count += freq_arr[i]
            max_star = max(max_star, count)
            # Update the frequency array
            freq_arr[num] += 1
        
        results.append(str(max_star))
    
    print('\n'.join(results))