import sys
import math

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
        # We need to choose which elements to flip to minimize the sum
        # The optimal strategy is to flip the smallest elements first
        # But we need to ensure that the sum of any contiguous subsequence of length > 1 is positive
        # So we need to flip the smallest elements, but not all of them
        # We can flip all elements except the largest one
        # Because if we flip all elements, the sum of any two adjacent elements would be negative
        # So we need to flip all elements except the largest one
        # So we sort the array, flip all elements except the largest one
        # This ensures that the sum of any two adjacent elements is positive
        # And the sum of any longer contiguous subsequence is also positive
        # Because the sum of any contiguous subsequence is the sum of the elements minus twice the sum of the flipped elements
        # So we need to flip the smallest elements to minimize the sum
        # So we sort the array, flip all elements except the largest one
        A_sorted = sorted(A)
        # Flip all elements except the largest one
        for i in range(N):
            if A_sorted[i] != A_sorted[-1]:
                B.append(-A_sorted[i])
            else:
                B.append(A_sorted[i])
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))