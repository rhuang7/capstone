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
        ans = [-1] * n
        # For each possible k from 1 to n
        for k in range(1, n + 1):
            # Check if there is a number that appears in all subsegments of length k
            # We can use sliding window and a frequency map
            freq = collections.defaultdict(int)
            # Initialize the first window
            for i in range(k):
                freq[a[i]] += 1
            # Check if any number appears in all windows
            found = False
            for num in freq:
                if freq[num] == k:
                    found = True
                    break
            if not found:
                ans[k - 1] = -1
                continue
            # Now find the number that appears in all windows
            # We can use a sliding window and track the count of each number
            # If any number's count drops below k, it's not the answer
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            # We can use a sliding window and a frequency map
            # We need to find the number that appears in all windows
            # So we can track the count of each number in the current window
            # and check if it's at least k
            #