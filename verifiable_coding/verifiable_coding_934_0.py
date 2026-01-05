import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        p = int(data[idx])
        q = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+p]))
        idx += p
        B = list(map(int, data[idx:idx+q]))
        idx += q
        C = list(map(int, data[idx:idx+r]))
        idx += r
        
        # Preprocess B to sort and compute prefix sums
        B_sorted = sorted(B)
        prefix_sum_B = [0] * (q + 1)
        for i in range(q):
            prefix_sum_B[i+1] = (prefix_sum_B[i] + B_sorted[i]) % MOD
        
        # Preprocess C to sort and compute prefix sums
        C_sorted = sorted(C)
        prefix_sum_C = [0] * (r + 1)
        for i in range(r):
            prefix_sum_C[i+1] = (prefix_sum_C[i] + C_sorted[i]) % MOD
        
        # Compute the sum for each element in B
        total = 0
        for y in B:
            # Find elements in A <= y
            left = 0
            right = p - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] <= y:
                    left = mid + 1
                else:
                    right = mid - 1
            count_A = left
            sum_A = sum(A[:left])
            
            # Find elements in C >= y
            left = 0
            right = r - 1
            while left <= right:
                mid = (left + right) // 2
                if C[mid] >= y:
                    right = mid - 1
                else:
                    left = mid + 1
            count_C = r - left
            sum_C = sum(C[left:])
            
            # Compute (sum_A) * (sum_C) and add to total
            term = (sum_A * sum_C) % MOD
            total = (total + term) % MOD
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()