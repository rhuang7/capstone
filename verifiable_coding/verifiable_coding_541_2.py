import sys
import collections

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
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_height = 0
        
        for i in range(N):
            color_count = collections.defaultdict(int)
            color_count[C[i]] = 1
            for j in range(i+1, N):
                color_count[C[j]] += 1
                if color_count[C[j]] % 2 == 0:
                    max_height = max(max_height, (color_count[C[j]] // 2) - 1)
                else:
                    max_height = max(max_height, (color_count[C[j]] // 2))
                if j - i + 1 > 2 * max_height + 1:
                    break
        
        results.append(str(max_height))
    
    print('\n'.join(results))