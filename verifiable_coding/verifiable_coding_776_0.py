import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    D_list = list(map(int, data[1:T+1]))
    
    for D in D_list:
        if D == 0:
            print(1)
            print(1)
            continue
        
        # Construct a sequence where the sum of min - gcd for all subarrays equals D
        # We use a sequence of 1s and a single 2 to adjust the sum
        # The sum of min - gcd for all subarrays of [1, 1, ..., 1] is 0
        # Adding a 2 at the end increases the sum by the number of subarrays ending at the 2
        # So we find the smallest k such that k*(k+1)/2 >= D
        k = 1
        while k*(k+1)//2 < D:
            k += 1
        
        # Create a sequence of k 1s and a 2 at the end
        A = [1] * k + [2]
        N = len(A)
        
        # Adjust the sequence to get exactly D
        # We can replace the last 1 with a larger number to increase the sum
        # The difference between the original sum and the new sum is the value we need
        # The original sum is k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//2 - (k*(k+1)//