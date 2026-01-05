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
        B.sort()
        prefix_B = [0] * (q + 1)
        for i in range(q):
            prefix_B[i+1] = (prefix_B[i] + B[i]) % MOD
        
        # Preprocess C to sort and compute prefix sums
        C.sort()
        prefix_C = [0] * (r + 1)
        for i in range(r):
            prefix_C[i+1] = (prefix_C[i] + C[i]) % MOD
        
        # Compute sum for each element in B
        total = 0
        for y in B:
            # Find number of elements in A <= y
            left_A = 0
            right_A = p - 1
            while left_A <= right_A:
                mid = (left_A + right_A) // 2
                if A[mid] <= y:
                    left_A = mid + 1
                else:
                    right_A = mid - 1
            count_A = left_A
            
            # Find number of elements in C >= y
            left_C = 0
            right_C = r - 1
            while left_C <= right_C:
                mid = (left_C + right_C) // 2
                if C[mid] >= y:
                    right_C = mid - 1
                else:
                    left_C = mid + 1
            count_C = r - left_C
            
            # Compute sum of A elements <= y
            sum_A = prefix_B[count_A] if count_A > 0 else 0
            
            # Compute sum of C elements >= y
            sum_C = (prefix_C[r] - prefix_C[left_C]) % MOD
            
            # Add to total: (sum_A + y) * (y + sum_C)
            term = ((sum_A + y) % MOD) * ((y + sum_C) % MOD)
            total = (total + term) % MOD
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()