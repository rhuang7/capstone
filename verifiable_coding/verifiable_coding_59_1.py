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
        possible_ks = set()
        
        for i in range(len(missing_positions) - 1):
            left = missing_positions[i]
            right = missing_positions[i + 1]
            left_val = a[left - 1] if left > 0 else None
            right_val = a[right + 1] if right < n - 1 else None
            
            if left_val is not None and right_val is not None:
                possible_ks.add(left_val)
                possible_ks.add(right_val)
                possible_ks.add(left_val + right_val)
                possible_ks.add(abs(left_val - right_val))
                possible_ks.add((left_val + right_val) // 2)
                possible_ks.add((left_val + right_val + 1) // 2)
                possible_ks.add((left_val + right_val - 1) // 2)
                possible_ks.add((left_val + right_val + 2) // 2)
                possible_ks.add((left_val + right_val - 2) // 2)
            
            if left_val is not None:
                possible_ks.add(left_val)
                possible_ks.add(left_val + 1)
                possible_ks.add(left_val - 1)
                possible_ks.add(left_val + 2)
                possible_ks.add(left_val - 2)
            
            if right_val is not None:
                possible_ks.add(right_val)
                possible_ks.add(right_val + 1)
                possible_ks.add(right_val - 1)
                possible_ks.add(right_val + 2)
                possible_ks.add(right_val - 2)
        
        if not possible_ks:
            possible_ks.add(0)
        
        min_m = float('inf')
        best_k = 0
        
        for k in possible_ks:
            new_a = a.copy()
            for i in range(n):
                if new_a[i] == -1:
                    new_a[i] = k
            current_m = 0
            for i in range(n - 1):
                current_m = max(current_m, abs(new_a[i] - new_a[i + 1]))
            if current_m < min_m:
                min_m = current_m
                best_k = k
        
        results.append(f"{min_m} {best_k}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()