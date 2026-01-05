import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx+1])
        idx += 2
        
        # Initialize the product of all steps
        total = 0
        current_product = 1
        
        for i in range(1, N+1):
            # Step i: remove i elements from the first column and i elements from the row i
            # But the first element of the row is already removed in the first part
            # So total elements removed in this step is 2i - 1
            # The product for this step is (A)^(2i-1)
            # But since the remaining elements are multiplied by p_i, we need to track the product
            # of all p_i's
            # However, since all elements are multiplied by p_i, the total product is the product of all p_i's
            # But the sum is the sum of p_i's
            # So we compute p_i as (A)^(2i-1)
            # And add it to the total
            p_i = pow(A, 2*i - 1, MOD)
            total = (total + p_i) % MOD
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()