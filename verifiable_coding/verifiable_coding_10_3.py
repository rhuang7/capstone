import sys
import bisect

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
        
        # Create a position map for quick lookup
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i
        
        # Find the maximum distance between two elements
        max_dist = 0
        best = []
        for i in range(1, n + 1):
            # Find the farthest element from i
            left = 1
            right = n
            while left < right:
                mid = (left + right) // 2
                if pos[mid] < pos[i]:
                    left = mid + 1
                else:
                    right = mid
            far_left = left
            left = 1
            right = n
            while left < right:
                mid = (left + right) // 2
                if pos[mid] > pos[i]:
                    right = mid
                else:
                    left = mid + 1
            far_right = left
            
            # Check if the farthest element is not i
            if far_left != i and far_right != i:
                dist = abs(pos[far_left] - pos[i]) + abs(pos[far_right] - pos[i])
                if dist > max_dist:
                    max_dist = dist
                    best = [p[far_left - 1], p[far_right - 1]]
                elif dist == max_dist:
                    # Choose the one with smaller length
                    if len(best) == 2:
                        best = [p[far_left - 1], p[far_right - 1]]
            elif far_left != i:
                dist = abs(pos[far_left] - pos[i])
                if dist > max_dist:
                    max_dist = dist
                    best = [p[far_left - 1], p[i - 1]]
                elif dist == max_dist:
                    if len(best) == 2:
                        best = [p[far_left - 1], p[i - 1]]
            elif far_right != i:
                dist = abs(pos[far_right] - pos[i])
                if dist > max_dist:
                    max_dist = dist
                    best = [p[far_right - 1], p[i - 1]]
                elif dist == max_dist:
                    if len(best) == 2:
                        best = [p[far_right - 1], p[i - 1]]
        
        # If no two elements found (should not happen as n >= 2)
        if not best:
            best = [p[0], p[1]]
        
        results.append(str(len(best)))
        results.append(' '.join(map(str, best)))
    
    print('\n'.join(results))