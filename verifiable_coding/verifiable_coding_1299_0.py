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
        
        for i in range(N):
            count[A[i]].append(i)
        
        max_dishes = -1
        best_type = None
        
        for typ in count:
            positions = count[typ]
            n = len(positions)
            if n == 0:
                continue
            # Maximum number of non-adjacent dishes
            # This is equivalent to the maximum number of non-adjacent elements in a list
            # which can be found by greedily selecting every other element
            # So the maximum is (n + 1) // 2
            max_dishes_type = (n + 1) // 2
            if max_dishes_type > max_dishes:
                max_dishes = max_dishes_type
                best_type = typ
            elif max_dishes_type == max_dishes:
                if typ < best_type:
                    best_type = typ
        
        results.append(str(best_type))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()