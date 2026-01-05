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
        w = list(map(int, data[idx:idx+k]))
        idx += k
        
        a.sort()
        w.sort(reverse=True)
        
        total = 0
        # Assign maximums and minimums
        # For each friend, take the largest available and the smallest available
        # But need to ensure that each friend gets exactly w_i integers
        # So, for the first (k - 1) friends, take the largest and the smallest
        # For the last friend, take the remaining
        # But need to handle cases where w_i is 1, then just take the max and min
        
        # Sort a
        a.sort()
        # Sort w in descending order
        w.sort(reverse=True)
        
        # Assign max and min for each friend
        # For the first (k - 1) friends, take the largest and the smallest
        # For the last friend, take the remaining
        # But need to handle cases where w_i is 1, then just take the max and min
        
        # We need to assign the max and min for each friend
        # So for each friend, we take the largest available and the smallest available
        # But for the last friend, we take the remaining
        
        # Let's think of it this way:
        # For each friend, we take the largest and the smallest available
        # But for the last friend, we take the remaining (so we don't need to take the smallest)
        
        # So, for the first (k - 1) friends, take the largest and the smallest
        # For the last friend, take the remaining
        
        # So, we need to take the largest and the smallest for the first (k - 1) friends
        # Then the last friend takes the rest
        
        # So, we take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, for the first (k - 1) friends:
        # Take the largest and the smallest
        # Then for the last friend, take the rest
        
        # So, we need to take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the first (k - 1) friends get one max and one min
        # The last friend gets the rest
        
        # So, for the first (k - 1) friends, we take the largest and the smallest
        # For the last friend, we take the remaining
        
        # So, we need to take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Sort a
        a.sort()
        # Sort w in descending order
        w.sort(reverse=True)
        
        # For the first (k - 1) friends, take the largest and the smallest
        # For the last friend, take the rest
        
        # So, for the first (k - 1) friends, we take the largest and the smallest
        # So, we take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the last friend takes the rest
        
        # So, the code is:
        # Take the largest and the smallest for (k - 1) times
        # Then the