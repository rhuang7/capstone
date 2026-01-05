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
        
        # Sort the array
        A_sorted = sorted(A)
        
        # Check if there's a valid p
        possible = False
        perm = []
        
        # Try to find a p where the first p elements are strictly increasing and the rest are strictly decreasing
        for p in range(1, N+1):
            # Check if first p elements are strictly increasing
            inc = True
            for i in range(p-1):
                if A_sorted[i] >= A_sorted[i+1]:
                    inc = False
                    break
            if not inc:
                continue
            
            # Check if the rest are strictly decreasing
            dec = True
            for i in range(p, N):
                if A_sorted[i] <= A_sorted[i+1]:
                    dec = False
                    break
            if dec:
                possible = True
                perm = A_sorted[:p] + A_sorted[p:]
                break
        
        if possible:
            results.append("YES")
            results.append(' '.join(map(str, perm)))
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()