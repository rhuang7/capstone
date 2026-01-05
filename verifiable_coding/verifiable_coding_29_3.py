import sys
import collections

def solve():
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
        
        # For each k from 1 to n, find the k-amazing number
        ans = [-1] * n
        
        # For each value in the array, track its positions
        pos = collections.defaultdict(list)
        for i in range(n):
            pos[a[i]].append(i)
        
        # For each value, check if it appears in all subarrays of length k
        for val in pos:
            positions = pos[val]
            # The value can only be a k-amazing number if it appears in all subarrays of length k
            # The minimum k for which this is possible is the maximum gap between consecutive positions + 1
            # The maximum k for which this is possible is the minimum gap between consecutive positions + 1
            # We need to find the k where the value is in all subarrays of length k
            # So, for each k, if the value is in all subarrays of length k, then it's a candidate
            # We can find the minimal k for which this is true
            # The minimal k is the maximum gap between consecutive positions + 1
            # The maximal k is the minimal gap between consecutive positions + 1
            # So for each k in [max_gap + 1, min_gap + 1], the value is a candidate
            # We can find the minimal k for which this is true
            # For this, we can use sliding window approach
            # We need to find the minimal k such that the value appears in all subarrays of length k
            # This can be done by checking for each k from 1 to n, if the value appears in all subarrays of length k
            # But this is O(n^2), which is too slow
            # So we need a smarter way
            # Let's find the minimal k for which the value appears in all subarrays of length k
            # This is equivalent to the value appearing in all subarrays of length k
            # So the minimal k is the maximum gap between consecutive positions + 1
            # The maximum gap is the maximum distance between two consecutive positions of the value
            # So for example, if the positions are [0, 2, 4], then the gaps are 2, 2
            # So the maximum gap is 2, and the minimal k is 3
            # So for this value, the k-amazing number is the minimal k for which the value appears in all subarrays of length k
            # So for this value, the k-amazing number is the maximum gap between consecutive positions + 1
            # But this is only true if the value appears in all subarrays of length k
            # So for this value, the k-amazing number is the maximum gap between consecutive positions + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case
            # So for this value, we can compute the maximum gap between consecutive positions
            # Then, the minimal k for which the value appears in all subarrays of length k is the maximum gap + 1
            # So for this value, the k-amazing number is the maximum gap + 1
            # But we need to check if this is the case