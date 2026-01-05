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
        
        # For each element in B, find valid X and Z
        total = 0
        for y in B:
            # Find all X in A where X <= y
            left = 0
            right = p - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] <= y:
                    left = mid + 1
                else:
                    right = mid - 1
            count_X = left
            sum_X = 0
            for i in range(count_X):
                sum_X = (sum_X + A[i]) % MOD
            
            # Find all Z in C where Z >= y
            left = 0
            right = r - 1
            while left <= right:
                mid = (left + right) // 2
                if C[mid] >= y:
                    right = mid - 1
                else:
                    left = mid + 1
            count_Z = r - left
            sum_Z = 0
            for i in range(left, r):
                sum_Z = (sum_Z + C[i]) % MOD
            
            # Compute (X + Y) * (Y + Z)
            term = ((sum_X + y) % MOD) * ((y + sum_Z) % MOD)
            total = (total + term) % MOD
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()