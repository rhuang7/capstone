import sys

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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        missing_positions = [i for i in range(n) if a[i] == -1]
        m = 0
        candidates = []
        
        for i in range(len(missing_positions) - 1):
            left = missing_positions[i]
            right = missing_positions[i + 1]
            left_val = a[left - 1] if left > 0 else None
            right_val = a[right + 1] if right < n - 1 else None
            
            if left_val is not None and right_val is not None:
                candidates.append((left_val, right_val))
            elif left_val is not None:
                candidates.append((left_val, None))
            elif right_val is not None:
                candidates.append((None, right_val))
        
        if not candidates:
            results.append("0 0")
            continue
        
        min_m = float('inf')
        best_k = 0
        
        for left, right in candidates:
            if left is None:
                left = -1
            if right is None:
                right = -1
            if left == right:
                continue
            low = min(left, right)
            high = max(left, right)
            if high - low < min_m:
                min_m = high - low
                best_k = low
            elif high - low == min_m:
                if low < best_k:
                    best_k = low
        
        results.append(f"{min_m} {best_k}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()