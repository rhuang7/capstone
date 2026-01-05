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
        
        # Construct a sequence that satisfies the condition
        # We use a sequence of numbers where each number is 1 more than the previous
        # This ensures that the min and GCD for any subarray are easy to compute
        # and the difference can be controlled
        N = 1
        A = [1]
        total = 0
        
        while total < D:
            N += 1
            A.append(N)
            # Compute the contribution of the new element to the total
            # We calculate the sum for all subarrays ending at the new element
            # This is O(N^2) in worst case, but we can optimize it
            # Here we use a simple approach for small N
            new_total = 0
            for i in range(N-1, -1, -1):
                current_min = min(A[i:N])
                current_gcd = math.gcd(A[i], A[i+1])
                for j in range(i+1, N):
                    current_gcd = math.gcd(current_gcd, A[j])
                    new_total += (current_min - current_gcd)
            total += new_total
        
        print(N)
        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()