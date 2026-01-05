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
        
        # Check if there are duplicates
        has_duplicates = len(set(A)) != N
        
        if has_duplicates:
            results.append("NO")
            continue
        
        # Check if the sorted array is strictly increasing
        is_increasing = all(A_sorted[i] < A_sorted[i+1] for i in range(N-1))
        
        if is_increasing:
            results.append("YES")
            results.append(' '.join(map(str, A_sorted)))
            continue
        
        # Check if the reversed sorted array is strictly decreasing
        is_decreasing = all(A_sorted[i] > A_sorted[i+1] for i in range(N-1))
        
        if is_decreasing:
            results.append("YES")
            results.append(' '.join(map(str, A_sorted[::-1])))
            continue
        
        # Check if there exists a peak point
        peak = -1
        for i in range(N-1):
            if A_sorted[i] > A_sorted[i+1]:
                peak = i
                break
        
        if peak == -1:
            results.append("NO")
            continue
        
        # Construct the permutation
        # First part: increasing up to peak
        # Second part: decreasing from peak
        # We can use the peak as the maximum element
        # So the first part is the first peak+1 elements
        # The second part is the remaining elements in reverse
        # But we need to ensure that the first part is strictly increasing
        # and the second part is strictly decreasing
        
        # Create the permutation
        perm = []
        # First part: increasing up to peak
        perm += A_sorted[:peak+1]
        # Second part: decreasing from peak
        perm += A_sorted[peak+1:][::-1]
        
        # Check if the permutation is valid
        is_valid = True
        for i in range(N-1):
            if perm[i] <= perm[i+1]:
                is_valid = False
                break
        
        if is_valid:
            results.append("YES")
            results.append(' '.join(map(str, perm)))
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()