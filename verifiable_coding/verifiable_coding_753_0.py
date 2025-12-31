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
        
        # Check for same type
        # Maple
        total_maple = MG + MY + MR
        if total_maple > 0:
            max_leaves = max(max_leaves, total_maple - (total_maple % 2))
        # Oak
        total_oak = OG + OY + OR
        if total_oak > 0:
            max_leaves = max(max_leaves, total_oak - (total_oak % 2))
        # Poplar
        total_poplar = PG + PY + PR
        if total_poplar > 0:
            max_leaves = max(max_leaves, total_poplar - (total_poplar % 2))
        
        # Check for same color
        # Green
        total_green = MG + OG + PG
        if total_green > 0:
            max_leaves = max(max_leaves, total_green - (total_green % 2))
        # Yellow
        total_yellow = MY + OY + PY
        if total_yellow > 0:
            max_leaves = max(max_leaves, total_yellow - (total_yellow % 2))
        # Red
        total_red = MR + OR + PR
        if total_red > 0:
            max_leaves = max(max_leaves, total_red - (total_red % 2))
        
        results.append(str(max_leaves))
    
    print('\n'.join(results)) 

if __name__ == '__main__':
    solve()