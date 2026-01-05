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
        
        # We need to find the maximum number of creatures that can be paid back
        # Each creature requires exactly Ai rupees, and we have P one-rupee coins and Q two-rupee coins
        # So for each creature, we need to check if we can pay Ai using the coins we have
        
        # Sort the array A
        A.sort()
        
        # We will try to select as many as possible creatures, starting from the smallest Ai
        # We can use a greedy approach: try to pay the smallest Ai first
        # We will use a binary search approach to find the maximum number of creatures that can be paid back
        
        # We will use a two-pointer approach to find the maximum number of creatures
        # We can use a binary search on the number of creatures
        low = 0
        high = N
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            # Try to select mid creatures
            # We will try to select the smallest mid creatures
            # Check if we can pay for them
            total = 0
            count = 0
            for i in range(mid):
                ai = A[i]
                # We need to pay ai rupees
                # We can use one-rupee coins and two-rupee coins
                # Let's try to use as many two-rupee coins as possible
                # The number of two-rupee coins needed is (ai // 2)
                # But we can't use more than Q two-rupee coins
                # So we can use min(ai // 2, Q) two-rupee coins
                # The remaining amount is ai - min(ai // 2, Q) * 2
                # We need to check if we have enough one-rupee coins
                two = min(ai // 2, Q)
                one = ai - two * 2
                if one <= P:
                    count += 1
                    P -= one
                    Q -= two
                else:
                    break
            if count == mid:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(best)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()