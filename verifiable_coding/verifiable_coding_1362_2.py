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
        # We need to flip the sign of some elements to minimize the sum
        # The optimal strategy is to flip the sign of the smallest elements
        # except for the smallest one (to avoid having two negative elements)
        # Sort the array
        sorted_A = sorted(A)
        # Flip the sign of all elements except the smallest one
        # So that the sum is minimized
        # But we need to ensure that any contiguous subsequence of length >1 has positive sum
        # So we can only flip the sign of elements except the smallest one
        # So we flip the sign of all elements except the smallest one
        # So the smallest element remains positive
        # The rest are flipped
        min_val = sorted_A[0]
        for num in A:
            if num != min_val:
                B.append(-num)
            else:
                B.append(num)
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))