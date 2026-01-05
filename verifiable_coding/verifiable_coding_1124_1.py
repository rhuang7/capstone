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
        
        # For each creature, the exact fare is Ai, and we need to pay exactly Ai
        # So we need to find a subset of A where sum of Ai is <= P + 2*Q
        # And for each Ai, we need to find a way to pay it using the coins
        # We can use a greedy approach: sort A in ascending order and try to pay as many as possible
        
        A.sort()
        total = 0
        count = 0
        for a in A:
            # Check if we can pay this creature
            # We need to find how many 1-rupee coins and 2-rupee coins we can use
            # We try to use as many 2-rupee coins as possible first
            # Then fill the rest with 1-rupee coins
            # If we can't pay, skip this creature
            # If we can, subtract the coins used and add to count
            # We need to check if a can be formed with the available coins
            # We can use binary search to find the maximum number of 2-rupee coins we can use
            # For a given a, the maximum number of 2-rupee coins is min(a // 2, Q)
            # Then the remaining amount is a - 2 * num_2_coins
            # We need to check if the remaining amount can be covered by 1-rupee coins
            # If yes, subtract the coins and add to count
            # If no, skip this creature
            # We can use binary search to find the maximum number of 2-rupee coins we can use
            # Let's try to find the maximum number of 2-rupee coins we can use for this a
            # The maximum number of 2-rupee coins is min(a // 2, Q)
            # We can try to use as many as possible
            # But we also need to make sure that the remaining amount can be covered by 1-rupee coins
            # So we can try to find the maximum number of 2-rupee coins that can be used
            # Let's try to find the maximum number of 2-rupee coins we can use for this a
            # Let's try to use as many as possible
            # We can use binary search to find the maximum number of 2-rupee coins
            # We can try to use x 2-rupee coins, then the remaining amount is a - 2*x
            # We need to check if the remaining amount is <= P
            # So we can binary search for the maximum x such that 2*x + (a - 2*x) <= P + 2*Q
            # But this is always true, since a <= P + 2*Q
            # So we can try to use as many 2-rupee coins as possible
            # So we can try to use min(a // 2, Q) 2-rupee coins
            # Then the remaining amount is a - 2 * num_2_coins
            # If that is <= P, we can use it
            # Else, we can't pay this creature
            # So we can try to use as many 2-rupee coins as possible
            # Let's try to find the maximum number of 2-rupee coins we can use for this a
            # Let's use binary search
            low = 0
            high = min(a // 2, Q)
            best = 0
            while low <= high:
                mid = (low + high) // 2
                rem = a - 2 * mid
                if rem <= P:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1
            # Now, best is the maximum number of 2-rupee coins we can use
            # The remaining amount is a - 2 * best
            rem = a - 2 * best
            if rem <= P:
                # We can pay this creature
                count += 1
                P -= rem
                Q -= best
        results.append(count)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()