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
        
        # Use a frequency array for faster access
        freq_arr = [0] * (max_val + 1)
        
        for num in A:
            # Count numbers divisible by num
            count = 0
            for multiple in range(num, max_val + 1, num):
                count += freq_arr[multiple]
            max_star = max(max_star, count)
            # Update frequency array
            freq_arr[num] += 1
        
        results.append(str(max_star))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()