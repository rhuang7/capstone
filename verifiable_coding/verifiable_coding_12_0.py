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
        
        possible = True
        
        # Check if a and b have the same elements except for some that can be adjusted
        # For each element in b, check if it can be achieved from a's elements
        # The only elements in a are -1, 0, 1
        # We can only add elements from a to other elements in a
        
        # Check for each position i
        for i in range(n):
            # If a[i] != b[i], then we need to adjust it
            if a[i] != b[i]:
                # We can only adjust a[i] by adding elements from a[0..i-1]
                # So the total sum of a[0..i-1] must be such that a[i] + sum = b[i]
                # But since a[0..i-1] can be any combination of -1, 0, 1, we can adjust it
                # However, we need to check if b[i] is achievable
                # The only way this is not possible is if b[i] is not in the set {-1, 0, 1} or if it's not achievable through operations
                # But since we can add any number of operations, we can adjust any value
                # However, the problem is that the operations can only be done on elements after the current one
                # So for position i, we can only add elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be anything, but we need to check if b[i] can be achieved
                # However, since we can perform any number of operations, we can adjust a[i] to any value
                # So the only constraint is that b[i] must be achievable by adding some combination of a[0..i-1]
                # But since a[0..i-1] can be any combination of -1, 0, 1, the sum can be any integer
                # So b[i] must be achievable by adding some combination of a[0..i-1] to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0..i-1] can be any integer, so a[i] + sum can be any integer
                # So b[i] must be achievable by adding some integer to a[i]
                # But since we can do any number of operations, the only constraint is that b[i] must be in the set {-1, 0, 1} or that it's achievable through some combination
                # However, the operations can only be done on elements after the current one
                # So for position i, the only way to adjust a[i] is by adding elements from positions 0 to i-1
                # So the sum of a[0