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
        color_count = collections.defaultdict(int)
        left = 0
        for right in range(N):
            color_count[C[right]] += 1
            
            while right - left + 1 > 2 * max_height + 1:
                color_count[C[left]] -= 1
                left += 1
            
            if right - left + 1 == 2 * max_height + 1:
                for color in color_count:
                    if color_count[color] % 2 == 0:
                        continue
                    else:
                        max_height = max(max_height, (color_count[color] - 1) // 2)
                        break
        
        results.append(str(max_height))
    
    print('\n'.join(results))