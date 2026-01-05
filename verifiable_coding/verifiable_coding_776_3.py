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
        
        # Construct a sequence where the sum of (min - gcd) over all subarrays equals D
        # We use a sequence of 1s and 2s, which allows us to control the sum
        # The idea is to have a sequence where the min is 1 and the gcd is 2, contributing -1 per subarray
        # We can adjust the length of the sequence to reach the desired D
        # The number of subarrays with min 1 and gcd 2 is (n*(n+1))/2 - (n-1)*n/2 = n
        # So we can use a sequence of n 1s and one 2 to get n subarrays contributing -1 each
        # So we need n = D
        N = D
        A = [1] * N
        A[-1] = 2
        print(N)
        print(' '.join(map(str, A)))
        
if __name__ == '__main__':
    solve()