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
        prefix_B = [0] * (q + 1)
        for i in range(q):
            prefix_B[i+1] = (prefix_B[i] + B_sorted[i]) % MOD
        
        # Preprocess C to sort and compute prefix sums
        C_sorted = sorted(C)
        prefix_C = [0] * (r + 1)
        for i in range(r):
            prefix_C[i+1] = (prefix_C[i] + C_sorted[i]) % MOD
        
        # For each element in B, find the number of elements in A <= B[i] and in C >= B[i]
        total = 0
        for y in B:
            # Find number of elements in A <= y
            a_count = 0
            left, right = 0, len(A)
            while left < right:
                mid = (left + right) // 2
                if A[mid] <= y:
                    left = mid + 1
                else:
                    right = mid
            a_count = left
            
            # Find number of elements in C >= y
            c_count = 0
            left, right = 0, len(C)
            while left < right:
                mid = (left + right) // 2
                if C[mid] >= y:
                    right = mid
                else:
                    left = mid + 1
            c_count = len(C) - left
            
            if a_count == 0 or c_count == 0:
                continue
            
            # Compute sum of (X + Y) for X in A <= Y
            sum_X_plus_Y = 0
            left, right = 0, len(A)
            while left < right:
                mid = (left + right) // 2
                if A[mid] <= y:
                    left = mid + 1
                else:
                    right = mid
            sum_X_plus_Y = (prefix_B[left] - prefix_B[0]) % MOD
            
            # Compute sum of (Y + Z) for Z in C >= Y
            sum_Y_plus_Z = 0
            left, right = 0, len(C)
            while left < right:
                mid = (left + right) // 2
                if C[mid] >= y:
                    right = mid
                else:
                    left = mid + 1
            sum_Y_plus_Z = (prefix_C[len(C)] - prefix_C[left]) % MOD
            
            # Compute contribution of this Y
            contribution = (sum_X_plus_Y * sum_Y_plus_Z) % MOD
            total = (total + contribution) % MOD
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()