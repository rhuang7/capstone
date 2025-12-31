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
        
        from collections import defaultdict
        type_positions = defaultdict(list)
        for i, typ in enumerate(A):
            type_positions[typ].append(i)
        
        max_count = -1
        best_type = None
        
        for typ in type_positions:
            positions = type_positions[typ]
            count = 0
            i = 0
            while i < len(positions):
                count += 1
                i += 2
            if count > max_count or (count == max_count and typ < best_type):
                max_count = count
                best_type = typ
        
        results.append(str(best_type))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()