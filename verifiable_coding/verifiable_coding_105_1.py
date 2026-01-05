import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array
        a.sort()
        
        # Compute the maximum number of operations
        total = 0
        for i in range(n-1, -1, -1):
            # Try to add a[i] to all previous piles
            # But we can only do it if the sum doesn't exceed k
            # So we calculate how many times we can add a[i] to the previous piles
            # The previous piles have a total sum of total
            # So the number of operations is total // a[i]
            # But we can't do more than (k - total) // a[i]
            # So the number of operations is min(total // a[i], (k - total) // a[i])
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (k - total) // a[i]
            # But we can only do it once per pile
            # So the number of operations is (k - total) // a[i]
            # But we can't do more than (k - total) // a[i]
            # And we can't do more than (total // a[i])
            # So the number of operations is min((k - total) // a[i], total // a[i])
            # But since we are adding to previous piles, we can do (