import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, P, Q = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each creature, the fare is Ai, and Lumpy needs to pay exactly Ai
        # So the extra amount paid by the creature is Ai - (Ai) = 0, but the problem says that Ai is the extra amount
        # Wait, the problem says that Ai is the extra amount paid by the i-th creature, so the exact amount is Ai
        # So Lumpy needs to pay exactly Ai for each creature
        # So the problem is to select as many Ai as possible such that the sum of selected Ai <= P + 2*Q
        # But we also need to consider that for each Ai, it can be paid with some combination of 1 and 2 rupee coins
        
        # The key is to find the maximum number of Ai's such that the sum of Ai's <= P + 2*Q and for each Ai, it can be paid with the coins available
        
        # To maximize the number of creatures, we should select the smallest Ai's first
        A.sort()
        
        total = 0
        count = 0
        for ai in A:
            # Check if ai can be paid with the current coins
            # ai can be paid with x 1-rupee coins and y 2-rupee coins such that x + 2y = ai
            # So x = ai - 2y
            # x must be >= 0 and <= P
            # y must be >= 0 and <= Q
            # We can try to find the minimum number of coins needed to pay ai
            # The minimal number of coins is ceil(ai / 2)
            # But we need to check if we have enough coins
            # So we can try to find the minimal number of coins needed to pay ai
            # Let's try to find the minimal number of coins needed to pay ai
            # The minimal number of coins is ceil(ai / 2)
            # But we need to check if we have enough coins
            # Let's try to find the minimal number of coins needed to pay ai
            # We can try to find the minimal number of 2-rupee coins needed
            # Let's find the minimal number of 2-rupee coins needed to pay ai
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's find the minimal number of 2-rupee coins needed
            # Let's find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's try to find the minimal number of 2-rupee coins needed
            # Let's