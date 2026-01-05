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
                candidates.append((abs(left_val - right_val), left_val, right_val))
            elif left_val is not None:
                candidates.append((abs(left_val - a[right]), left_val, a[right]))
            elif right_val is not None:
                candidates.append((abs(a[left] - right_val), a[left], right_val))
        
        if not candidates:
            results.append("0 0")
            continue
        
        min_m = min(candidates, key=lambda x: x[0])[0]
        possible_ks = set()
        
        for val, left, right in candidates:
            if val == min_m:
                if left is not None and right is not None:
                    possible_ks.add((left_val + right_val) // 2)
                elif left is not None:
                    possible_ks.add(left_val)
                elif right is not None:
                    possible_ks.add(right_val)
        
        results.append(f"{min_m} {min(possible_ks)}")
    
    print('\n'.join(results)) 

if __name__ == '__main__':
    solve()