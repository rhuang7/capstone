import sys
import random

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Count the number of inversions
    def count_inversions(arr):
        inv_count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    inv_count = count_inversions(perm)

    # Petr's method: 3n swaps
    # Alex's method: 7n + 1 swaps
    # The number of inversions is roughly proportional to the number of swaps
    # So we can compare the inversion count to expected values
    # For Petr: expected inversions is about 3n^2 / 4
    # For Alex: expected inversions is about (7n + 1) * n / 2
    petr_expected = 3 * n * n // 4
    umnik_expected = (7 * n + 1) * n // 2

    if inv_count < petr_expected:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()