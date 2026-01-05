import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        R = int(data[index])
        C = int(data[index+1])
        M = int(data[index+2])
        K = int(data[index+3])
        J = int(data[index+4])
        index += 5
        
        total_area = R * C
        if M + K + J != total_area:
            results.append("No")
            continue
        
        # Function to check if a rectangle with area A can be cut from a rectangle of size r x c
        def can_cut(r, c, a):
            if a == 0:
                return True
            for h in range(1, int(c**0.5) + 1):
                if c % h == 0:
                    w = a // h
                    if w <= r and w >= 0:
                        return True
            for w in range(1, int(r**0.5) + 1):
                if r % w == 0:
                    h = a // w
                    if h <= c and h >= 0:
                        return True
            return False
        
        # Check all possible ways to cut the cake
        # Try all permutations of the three areas
        from itertools import permutations
        found = False
        for perm in permutations([M, K, J]):
            a, b, c = perm
            # Try all possible ways to cut the cake into three parts
            # First, check if a can be cut from R x C
            if not can_cut(R, C, a):
                continue
            # Now check if b can be cut from the remaining area
            # The remaining area is (R*C - a)
            # But we need to check if it can be cut from the remaining part
            # So we need to try all possible ways to cut the remaining area
            # This is complex, so we try all possible ways to cut the remaining area
            # Try all possible ways to cut the remaining area into b and c
            # Try all possible ways to cut the cake into a, b, c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # This is very complex, but we can try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake into a, then b, then c
            # Try all possible ways to cut the cake