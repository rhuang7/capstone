import sys
import math
from collections import defaultdict

def compute_gcd_list(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
        if gcd == 1:
            break
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
                temp = []
                for num2 in freq:
                    if num2 != num and freq[num2] > 0:
                        temp.append(num2)
                if temp:
                    gcd2 = compute_gcd_list(temp)
                    max_sum = max(max_sum, current_gcd + gcd2)
        
        if max_sum == 0:
            max_sum = A[0] + A[1]
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()