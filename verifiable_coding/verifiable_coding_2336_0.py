import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Count the number of inversions
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv_count += 1

    # For Petr's method, the number of inversions is roughly O(n^2)
    # For Um_nik's method, the number of inversions is roughly O(n^2)
    # But the number of swaps is different, so we can use the expected number of inversions
    # Petr's method: 3n swaps, Um_nik's method: 7n + 1 swaps
    # The expected number of inversions after k swaps is roughly k * (n^2) / 2 / n = k * n / 2
    # So, for Petr: expected inversions ~ 3n * n / 2 = 1.5n^2
    # For Um_nik: expected inversions ~ (7n + 1) * n / 2 ≈ 3.5n^2

    # If inv_count is close to 1.5n^2, it's Petr's method
    # If inv_count is close to 3.5n^2, it's Um_nik's method
    # We can use a threshold to decide based on the ratio of inv_count to n^2
    # We'll use a threshold of 1.5 * n^2 and 3.5 * n^2

    # Compute the expected values
    petr_expected = 1.5 * n * n
    umnik_expected = 3.5 * n * n

    # Check which one is closer
    if inv_count < petr_expected + 1000000 or inv_count > umnik_expected - 1000000:
        # If it's far from both, it's likely Petr's method
        print("Petr")
    else:
        # Check which is closer
        petr_diff = abs(inv_count - petr_expected)
        umnik_diff = abs(inv_count - umnik_expected)
        if petr_diff < umnik_diff:
            print("Petr")
        else:
            print("Um_nik")