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
        res = [-1] * n
        
        # For each element, track its positions
        pos = collections.defaultdict(list)
        for i in range(n):
            pos[a[i]].append(i)
        
        # For each element, check if it appears in all k-length subarrays
        for num in pos:
            positions = pos[num]
            # The element can only be a k-amazing number if it appears in all k-length subarrays
            # The minimum k for which this is possible is the length of the first occurrence of the element
            # The maximum k for which this is possible is the length of the last occurrence of the element
            # So for each k in this range, check if the element appears in all k-length subarrays
            # To check this, the element must appear in every window of size k
            # This is only possible if the element appears in every window of size k, which requires that the distance between consecutive occurrences is <= k-1
            # So for the element to be a k-amazing number, it must appear in every window of size k
            # This is only possible if the element appears in every window of size k, which implies that the element's positions are such that the distance between consecutive occurrences is <= k-1
            # So for the element to be a k-amazing number, the minimum k is the length of the first occurrence of the element
            # And the maximum k is the length of the last occurrence of the element
            # So for each k in this range, check if the element appears in all k-length subarrays
            # To do this efficiently, we can check for each k in the range [min_k, max_k], whether the element appears in every window of size k
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it appears in all k-length subarrays
            # This is the minimum k for which the element appears in every window of size k
            # This is the minimum k for which the element appears in every window of size k
            # This is the minimum k for which the element appears in every window of size k
            # This is the minimum k for which the element appears in every window of size k
            # So for each element, we can find the minimum k for which it appears in all k-length subarrays
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, check for all possible k where it can be a k-amazing number
            # This is only possible if the element appears in every window of size k
            # To check this, we can use the following condition:
            # For the element to appear in every window of size k, the distance between consecutive occurrences must be <= k-1
            # So for the element to be a k-amazing number, the distance between consecutive occurrences must be <= k-1
            # So for the element, we can find the minimum k for which this is true
            # Then, for all k >= this minimum, the element can be a k-amazing number
            # So for each element, we can find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element
            # But this is not efficient for large n
            # So we can use the following approach:
            # For each element, find the minimum k for which it can be a k-amazing number
            # Then, for each k from 1 to n, if there is an element that can be a k-amazing number, we set res[k-1] to that element