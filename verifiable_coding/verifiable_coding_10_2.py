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
        
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i
        
        left = []
        right = []
        
        for i in range(n):
            val = p[i]
            idx_val = pos[val]
            # Find the first element in left with position < idx_val
            l = bisect.bisect_left(left, (idx_val, 0))
            if l > 0:
                left[l - 1] = (idx_val, val)
            else:
                left.append((idx_val, val))
        
        for i in range(n - 1, -1, -1):
            val = p[i]
            idx_val = pos[val]
            # Find the first element in right with position > idx_val
            r = bisect.bisect_right(right, (idx_val, 0))
            if r < len(right):
                right[r] = (idx_val, val)
            else:
                right.append((idx_val, val))
        
        left_result = []
        for val, _ in left:
            left_result.append(val)
        right_result = []
        for val, _ in right:
            right_result.append(val)
        
        if len(left_result) >= 2:
            left_result.reverse()
            left_result = left_result[:2]
        if len(right_result) >= 2:
            right_result = right_result[:2]
        
        if len(left_result) >= 2 and len(right_result) >= 2:
            if len(left_result) <= len(right_result):
                res = left_result
            else:
                res = right_result
        elif len(left_result) >= 2:
            res = left_result
        else:
            res = right_result
        
        results.append(str(len(res)))
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))