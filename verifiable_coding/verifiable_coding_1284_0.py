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
        
        # Try all possible thresholds
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    # Check if this partition is valid
                    d_count = 0
                    c_count = 0
                    b_count = 0
                    a_count = 0
                    
                    # Determine counts based on thresholds
                    x = A[i]
                    y = A[j]
                    z = A[k]
                    
                    for score in A:
                        if score < x:
                            d_count += 1
                        elif score < y:
                            c_count += 1
                        elif score < z:
                            b_count += 1
                        else:
                            a_count += 1
                    
                    if d_count == N // 4 and c_count == N // 4 and b_count == N // 4 and a_count == N // 4:
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