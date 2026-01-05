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
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        # For each dish, we can choose either a[i] or b[i]
        # We need to select which dishes to get by courier and which to pick up
        # The total time is the maximum of (a[i] for courier dishes) and (sum of b[i] for pick up dishes)
        # We need to minimize this maximum
        
        # We can try all possible subsets of dishes to get by courier, but that's too slow
        # Instead, we can try to choose the best combination of courier and pick up dishes
        
        # We can try to choose the k dishes with the smallest (a[i] - b[i]) to get by courier
        # Because for those dishes, a[i] - b[i] is the time saved by using courier instead of pick up
        # So we want to choose the dishes where a[i] - b[i] is smallest, as they give the most benefit
        
        # We sort the dishes by (a[i] - b[i])
        dishes = sorted(zip(a, b), key=lambda x: x[0] - x[1])
        
        # Try all possible numbers of dishes to get by courier (from 0 to n)
        # For each k, we take the first k dishes as courier, the rest as pick up
        # Compute the maximum between the maximum a[i] of courier dishes and the sum of b[i] of pick up dishes
        # Find the minimum of these maxima
        
        min_time = float('inf')
        for k in range(n + 1):
            # Take first k dishes as courier
            courier_a = [d[0] for d in dishes[:k]]
            # Take remaining as pick up
            pick_up_b = [d[1] for d in dishes[k:]]
            
            max_courier = max(courier_a) if courier_a else 0
            sum_pick_up = sum(pick_up_b) if pick_up_b else 0
            
            total_time = max(max_courier, sum_pick_up)
            if total_time < min_time:
                min_time = total_time
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()