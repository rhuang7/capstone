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
        # We can try to construct the permutation as follows:
        # - Find the peak element (the maximum element)
        # - Place it at position p (the peak)
        # - Arrange the elements to the left of the peak in increasing order
        # - Arrange the elements to the right of the peak in decreasing order
        
        # Find the peak element
        peak = A_sorted[-1]
        left = []
        right = []
        
        for num in A_sorted:
            if num == peak:
                # This is the peak element
                pass
            elif num < peak:
                left.append(num)
            else:
                right.append(num)
        
        # Now, we need to arrange left in increasing order and right in decreasing order
        # But we need to ensure that the peak is at the correct position
        # So we can try to place the peak at the end of the left part
        # and the right part in reverse order
        
        # Construct the permutation
        perm = []
        # Add the left part in increasing order
        for num in left:
            perm.append(num)
        # Add the peak
        perm.append(peak)
        # Add the right part in decreasing order
        for num in reversed(right):
            perm.append(num)
        
        # Check if the permutation is valid
        # The first part must be strictly increasing
        # The second part must be strictly decreasing
        # Also, the peak must be the maximum element
        # We can check this by verifying the conditions
        
        # Check if the permutation is valid
        is_valid = True
        for i in range(len(perm) - 1):
            if perm[i] >= perm[i + 1]:
                is_valid = False
                break
        
        if is_valid:
            results.append("YES")
            results.append(" ".join(map(str, perm)))
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()