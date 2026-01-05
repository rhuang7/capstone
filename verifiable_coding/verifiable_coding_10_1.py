import sys
import math

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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i
        
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        
        for i in range(1, n + 1):
            left[i] = left[i - 1] + 1 if pos[i] < pos[i - 1] else left[i - 1]
        
        for i in range(n, 0, -1):
            right[i] = right[i + 1] + 1 if pos[i] > pos[i + 1] else right[i + 1]
        
        max_sum = 0
        best = []
        for i in range(1, n + 1):
            if left[i] >= 2 or right[i] >= 2:
                if left[i] >= 2:
                    current = left[i] - 1
                    if current > max_sum:
                        max_sum = current
                        best = []
                        for j in range(i - (left[i] - 1), i + 1):
                            best.append(p[j - 1])
                    elif current == max_sum:
                        if len(best) > 0:
                            if len(best) > len([p[i - 1]] + best):
                                best = [p[i - 1]] + best
                if right[i] >= 2:
                    current = right[i] - 1
                    if current > max_sum:
                        max_sum = current
                        best = []
                        for j in range(i, i + (right[i] - 1) + 1):
                            best.append(p[j - 1])
                    elif current == max_sum:
                        if len(best) > 0:
                            if len(best) > len([p[i - 1]] + best):
                                best = [p[i - 1]] + best
        
        results.append(str(len(best)))
        results.append(' '.join(map(str, best)))
    
    print('\n'.join(results))