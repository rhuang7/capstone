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
        
        # Check if the array can be rearranged to satisfy the condition
        # We can try to construct the permutation as follows:
        # - The first part is strictly increasing
        # - The second part is strictly decreasing
        # We can try to find a peak element and arrange the array around it
        # However, for simplicity, we can check if the sorted array can be rearranged
        # such that there's a peak and the rest are arranged accordingly
        
        # Try to find a peak
        peak = -1
        for i in range(N):
            if i == 0:
                if A_sorted[i] < A_sorted[i+1]:
                    peak = i
            elif i == N-1:
                if A_sorted[i] > A_sorted[i-1]:
                    peak = i
            else:
                if A_sorted[i] > A_sorted[i-1] and A_sorted[i] > A_sorted[i+1]:
                    peak = i
                    break
        
        if peak == -1:
            # No peak found, check if the array is strictly increasing or decreasing
            if all(A_sorted[i] < A_sorted[i+1] for i in range(N-1)):
                results.append("YES")
                results.append(" ".join(map(str, A_sorted)))
            elif all(A_sorted[i] > A_sorted[i+1] for i in range(N-1)):
                results.append("YES")
                results.append(" ".join(map(str, A_sorted[::-1])))
            else:
                results.append("NO")
            continue
        
        # Construct the permutation
        # First part is strictly increasing up to the peak
        # Second part is strictly decreasing from the peak
        # We can use the sorted array and arrange it accordingly
        # We need to ensure that the peak is the maximum element
        # So we can take the sorted array and arrange it such that the peak is the maximum
        
        # Check if the maximum element is at the peak
        if A_sorted[-1] != A_sorted[peak]:
            results.append("NO")
            continue
        
        # Construct the permutation
        perm = []
        # First part: strictly increasing up to the peak
        perm.extend(A_sorted[:peak+1])
        # Second part: strictly decreasing from the peak
        perm.extend(A_sorted[peak+1:][::-1])
        
        # Check if the permutation is valid
        valid = True
        for i in range(N-1):
            if perm[i] <= perm[i+1]:
                valid = False
                break
        for i in range(N-1, 0, -1):
            if perm[i] <= perm[i-1]:
                valid = False
                break
        
        if valid:
            results.append("YES")
            results.append(" ".join(map(str, perm)))
        else:
            results.append("NO")
    
    # Output the results
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()