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
        
        # For each dish, choose the minimum between a_i and b_i
        # But we need to consider that some dishes must be picked up by Petya
        # So we need to select which dishes to use courier for to minimize the maximum time
        
        # We can try all possible combinations, but that's too slow
        # So we choose to use courier for the dishes where a_i < b_i
        # And pick up the rest
        # The maximum time will be the maximum of the courier times and the sum of the pick up times
        
        # Let's compute the maximum courier time and the sum of pick up times
        max_courier = 0
        sum_pickup = 0
        
        for i in range(n):
            if a[i] < b[i]:
                max_courier = max(max_courier, a[i])
            else:
                sum_pickup += b[i]
        
        # The total time is the maximum between the max courier time and the sum of pick up times
        results.append(str(max(max_courier, sum_pickup)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()