import sys

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
        
        A.sort()
        
        d_count = 0
        c_count = 0
        b_count = 0
        a_count = 0
        
        # Find the boundaries for each grade
        # D is < x
        # C is >=x and < y
        # B is >=y and < z
        # A is >=z
        
        # We need exactly N/4 students in each grade
        d_cut = N // 4
        c_cut = 2 * N // 4
        b_cut = 3 * N // 4
        a_cut = N
        
        # Determine x, y, z
        x = A[d_cut - 1] + 1
        y = A[c_cut - 1] + 1
        z = A[b_cut - 1] + 1
        
        # Check if the thresholds are valid
        valid = True
        for i in range(N):
            if A[i] < x:
                if i >= d_cut:
                    valid = False
                    break
            elif A[i] < y:
                if i >= d_cut and i < c_cut:
                    valid = False
                    break
            elif A[i] < z:
                if i >= d_cut and i < b_cut:
                    valid = False
                    break
            else:
                if i >= b_cut:
                    valid = False
                    break
        
        if valid:
            results.append(f"{x} {y} {z}")
        else:
            results.append("-1")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()