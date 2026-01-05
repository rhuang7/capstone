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
        
        # Find the thresholds
        x = 0
        y = 0
        z = 0
        found = False
        
        # Try all possible combinations of thresholds
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    # Check if the counts match
                    d_count = i
                    c_count = j - i
                    b_count = k - j
                    a_count = N - k
                    
                    if d_count == N//4 and c_count == N//4 and b_count == N//4 and a_count == N//4:
                        # Check if the thresholds are valid
                        x = A[i-1] + 1 if i > 0 else 0
                        y = A[j-1] + 1 if j > 0 else 0
                        z = A[k-1] + 1 if k > 0 else 0
                        # Ensure that the thresholds are in increasing order
                        if x < y < z:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        
        if found:
            results.append(f"{x} {y} {z}")
        else:
            results.append("-1")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()