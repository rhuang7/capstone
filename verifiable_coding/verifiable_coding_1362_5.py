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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = []
        # We need to choose which elements to flip
        # To minimize the sum, we want to flip the smallest elements
        # But we have to ensure that any contiguous subsequence of length > 1 has a positive sum
        # So, we flip the smallest elements, but not all of them
        # We flip the smallest elements in a way that ensures the condition is satisfied
        # We can flip the smallest element, then the next smallest, etc., but not all
        # The optimal strategy is to flip the smallest element, then the next smallest, etc., but not all
        # We can flip all elements except the largest one
        # Because if we flip all elements except the largest, then any contiguous subsequence of length > 1 will have a positive sum
        # Because the largest element is not flipped, and the rest are flipped, so the sum of any contiguous subsequence of length > 1 will be at least the largest element (which is not flipped)
        # So, we flip all elements except the largest one
        # So, we sort the array, and flip all elements except the largest one
        sorted_A = sorted(A)
        max_val = sorted_A[-1]
        for a in A:
            if a != max_val:
                B.append(-a)
            else:
                B.append(a)
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))