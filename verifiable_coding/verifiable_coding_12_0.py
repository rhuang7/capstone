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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Check if a and b have the same elements except for possible -1, 0, 1
        # For each element in b, it must be achievable by some combination of operations
        # The operations allow adding a_i to a_j, which can be used to adjust values
        # The key observation is that for each element in b, it must be possible to reach it
        # from the corresponding a_i through additions of other elements
        
        # First, check if the counts of -1, 0, 1 in a and b are compatible
        # For each element in b, it must be achievable by some combination of operations
        # The operations allow adding a_i to a_j, so the value of a_j can be adjusted
        # However, the value of a_i itself is fixed, so the operations can only affect a_j
        
        # For each position i, the value of b[i] must be achievable from a[i] through additions of other elements
        # The key is that for each i, the value of b[i] must be achievable by adding some number of a_j's (j != i)
        # Since a_j can be -1, 0, or 1, the value of b[i] must be achievable by adding some combination of these
        
        # The operations allow us to add any number of a_i's to a_j, so for each i, the value of b[i] must be achievable
        # by adding some number of a_i's to a[i]
        
        # However, the operations can be applied multiple times, so the value of b[i] must be achievable by some combination
        # of additions of a_i's to a[i]
        
        # For each i, the value of b[i] must be achievable by adding some number of a_i's to a[i]
        # Since a_i is fixed, the value of b[i] must be equal to a[i] + k * a_i, where k is some integer
        # This simplifies to b[i] = a[i] * (1 + k)
        # So, for each i, b[i] must be a multiple of a[i], or a[i] is 0
        
        # If a[i] is 0, then b[i] must be 0, because adding 0 to any value doesn't change it
        # If a[i] is -1 or 1, then b[i] must be a multiple of a[i]
        
        # So, for each i, if a[i] is not 0, then b[i] must be a multiple of a[i]
        
        # Also, for each i, the value of b[i] must be achievable by adding some number of a_i's to a[i]
        # This means that b[i] must be equal to a[i] + k * a[i], where k is an integer
        # Which is equivalent to b[i] = a[i] * (1 + k)
        # So, b[i] must be a multiple of a[i]
        
        # Also, for each i, if a[i] is 0, then b[i] must be 0
        
        # So, for each i, if a[i] is not 0, then b[i] must be a multiple of a[i]
        
        # Additionally, for each i, if a[i] is not 0, then b[i] must be achievable by adding some number of a_i's to a[i]
        # Which means that b[i] must be equal to a[i] + k * a[i], where k is an integer
        # Which is equivalent to b[i] = a[i] * (1 + k)
        # So, b[i] must be a multiple of a[i]
        
        # So, for each i, if a[i] is not 0, then b[i] must be a multiple of a[i]
        
        # Also, if a[i] is 0, then b[i] must be 0
        
        # So, for each i, if a[i] is not 0, then b[i] must be a multiple of a[i]
        
        # Now, check for each i
        possible = True
        for i in range(n):
            ai = a[i]
            bi = b[i]
            if ai == 0:
                if bi != 0:
                    possible = False
                    break
            else:
                if bi % ai != 0:
                    possible = False
                    break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()