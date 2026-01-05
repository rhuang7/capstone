import sys
import math
from collections import defaultdict

def compute_gcd_list(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_sum = 0
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        for num in freq:
            if freq[num] >= 2:
                current_gcd = num
                for i in range(1, num):
                    if freq[i] >= 2:
                        current_gcd = math.gcd(current_gcd, i)
                max_sum = max(max_sum, current_gcd + num)
        
        if len(freq) >= 2:
            max_sum = max(max_sum, freq[A[0]] + freq[A[1]])
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()