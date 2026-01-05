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
        type_count = defaultdict(list)
        for i, val in enumerate(A):
            type_count[val].append(i)
        max_dishes = -1
        best_type = None
        for typ in type_count:
            positions = type_count[typ]
            n = len(positions)
            if n == 0:
                continue
            # Max dishes that can be chosen without adjacency
            # This is equivalent to the maximum number of non-adjacent elements in a list
            # which is (n + 1) // 2
            max_dishes_type = (n + 1) // 2
            if max_dishes_type > max_dishes:
                max_dishes = max_dishes_type
                best_type = typ
            elif max_dishes_type == max_dishes:
                if typ < best_type:
                    best_type = typ
        results.append(str(best_type))
    print('\n'.join(results))