import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        # We need to check if the permutation can be split into two arrays a and b
        # such that merge(a, b) = p
        # The merge process is similar to merge sort, but with arbitrary order
        
        # We can simulate the merge process in reverse
        # Start from the end of the permutation and try to split it into a and b
        # The merge process is such that the first element of the merged array is the smaller of the first elements of a and b
        # So, in reverse, we can try to find where the split between a and b occurs
        
        # We'll use a greedy approach to find the split
        # We'll keep track of the current elements of a and b
        # We'll try to find the split by checking which element comes first in the merge process
        
        # We'll simulate the merge in reverse
        # Start from the end of the permutation and work backwards
        # We'll keep track of the current elements of a and b
        # We'll try to find the split by checking which element comes first in the merge process
        
        # Initialize a and b as empty lists
        a = []
        b = []
        # Start from the end of the permutation
        i = 2 * n - 1
        # We'll keep track of the current elements of a and b
        # We'll use a pointer for a and b
        a_ptr = 0
        b_ptr = 0
        
        # We'll iterate backwards through the permutation
        while i >= 0:
            # Check if a is not empty and b is not empty
            if a and b:
                # Compare the current elements of a and b
                if a[0] < b[0]:
                    # The first element of the merged array is a[0]
                    # So, the current element in the permutation is a[0]
                    # So, we remove a[0] from a
                    a.pop(0)
                    a_ptr -= 1
                else:
                    # The first element of the merged array is b[0]
                    # So, the current element in the permutation is b[0]
                    # So, we remove b[0] from b
                    b.pop(0)
                    b_ptr -= 1
            elif a:
                # The first element of the merged array is a[0]
                # So, the current element in the permutation is a[0]
                # So, we remove a[0] from a
                a.pop(0)
                a_ptr -= 1
            elif b:
                # The first element of the merged array is b[0]
                # So, the current element in the permutation is b[0]
                # So, we remove b[0] from b
                b.pop(0)
                b_ptr -= 1
            else:
                # Both a and b are empty
                # This is only possible if the permutation is empty
                break
            
            i -= 1
        
        # After processing, a and b should both be of length n
        if len(a) == n and len(b) == n:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()