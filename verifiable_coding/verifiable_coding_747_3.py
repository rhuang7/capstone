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
        
        # Check if there is a valid permutation
        # We can try to create a permutation where the first part is strictly increasing and the second is strictly decreasing
        # We can use the sorted array and try to construct the permutation
        
        # Try to find a peak element
        peak = -1
        for i in range(N):
            if i == 0:
                if A_sorted[i] < A_sorted[i+1]:
                    peak = i
            elif i == N-1:
                if A_sorted[i-1] > A_sorted[i]:
                    peak = i
            else:
                if A_sorted[i-1] < A_sorted[i] and A_sorted[i] > A_sorted[i+1]:
                    peak = i
                    break
        
        if peak == -1:
            # No peak found, check if the array is strictly increasing or strictly decreasing
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
        # First part is strictly increasing up to peak, then strictly decreasing
        # We can take the first part as the first (peak + 1) elements, then the rest in reverse
        # But need to ensure that the peak is the maximum element
        # So we can take the first (peak + 1) elements as the increasing part
        # Then the rest in reverse order
        
        # Check if the peak is the maximum element
        if A_sorted[peak] != max(A_sorted):
            results.append("NO")
            continue
        
        # Construct the permutation
        perm = A_sorted[:peak+1] + A_sorted[peak+1:][::-1]
        
        # Check if the permutation is valid
        valid = True
        for i in range(N-1):
            if perm[i] <= perm[i+1]:
                valid = False
                break
        if valid:
            results.append("YES")
            results.append(" ".join(map(str, perm)))
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()