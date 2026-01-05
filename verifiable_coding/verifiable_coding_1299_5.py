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
        count = defaultdict(list)
        
        for i, a in enumerate(A):
            count[a].append(i)
        
        max_dishes = -1
        best_type = None
        
        for typ, positions in count.items():
            # Calculate max non-adjacent dishes
            prev = -2
            curr = 0
            for pos in positions:
                if pos >= prev + 2:
                    curr += 1
                    prev = pos
            if curr > max_dishes:
                max_dishes = curr
                best_type = typ
            elif curr == max_dishes and best_type is None:
                best_type = typ
        
        results.append(str(best_type))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()