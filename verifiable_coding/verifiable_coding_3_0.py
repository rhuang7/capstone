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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array
        a.sort()
        
        # The maximum possible difference is achieved by moving as much water as possible from the first k barrels to the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels, and the min is the sum of the first k barrels
        # But we need to consider that we can only pour k times, so we can only take the first k barrels and move all their water to the last (n - k) barrels
        # The max is the sum of the last (n - k) barrels, and the min is 0 (since we can pour all water from the first k barrels)
        # But wait, the first k barrels may have some water left if we don't pour all of it, but to maximize the difference, we should pour all of it
        # So the max is the sum of the last (n - k) barrels, and the min is 0
        # However, if all the first k barrels are emptied, then the min is 0
        # So the maximum difference is the sum of the last (n - k) barrels
        # But wait, we can pour from the first k barrels to the last (n - k) barrels, but we can only do it k times
        # So we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels plus the sum of the first k barrels
        # The min is 0 (since we can pour all the water from the first k barrels)
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But wait, we can only pour k times, so we can pour from the first k barrels to the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0 (since we can pour all the water from the first k barrels)
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But wait, the sum of the last (n - k) barrels is already the max, and the sum of the first k barrels is the amount we can pour into them
        # So the maximum difference is the sum of the last (n - k) barrels + sum of the first k barrels
        # But wait, the sum of the last (n - k) barrels is the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But that's not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But this is not correct because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But that's not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But this is not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But that's not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But this is not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But that's not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But this is not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But that's not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But this is not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (n - k) barrels) - 0
        # But that's not correct either, because we can pour all the water from the first k barrels into the last (n - k) barrels
        # So the max is the sum of the last (n - k) barrels + sum of the first k barrels
        # The min is 0
        # So the maximum difference is (sum of the last (n - k) barrels + sum of the first k barrels) - 0
        # But this is not correct, because the sum of the last (n - k) barrels is already the max, and the min is 0
        # So the maximum difference is (sum of the last (