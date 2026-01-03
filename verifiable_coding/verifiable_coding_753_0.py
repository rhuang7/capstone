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
        # Read maple leaves
        MG = int(data[idx])
        MY = int(data[idx+1])
        MR = int(data[idx+2])
        idx += 3
        
        # Read oak leaves
        OG = int(data[idx])
        OY = int(data[idx+1])
        OR = int(data[idx+2])
        idx += 3
        
        # Read poplar leaves
        PG = int(data[idx])
        PY = int(data[idx+1])
        PR = int(data[idx+2])
        idx += 3
        
        max_leaves = 0
        
        # Check by type
        # Maple
        total = MG + MY + MR
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        # Oak
        total = OG + OY + OR
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        # Poplar
        total = PG + PY + PR
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        
        # Check by color
        # Green
        total = MG + OG + PG
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        # Yellow
        total = MY + OY + PY
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        # Red
        total = MR + OR + PR
        if total > 0:
            if total % 2 == 1:
                max_leaves = max(max_leaves, total)
            else:
                max_leaves = max(max_leaves, total - 1)
        
        results.append(str(max_leaves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()