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
    # So if inv_count is small, it's more likely to be Petr's method
    # If inv_count is large, it's more likely to be Alex's method

    # For large n, the expected number of inversions in a random permutation is n*(n-1)/4
    # So we can compare inv_count to this value
    expected_petr = n * (n - 1) // 4
    expected_alex = n * (n - 1) // 4 * 2  # Approximate for 7n+1 swaps

    if inv_count < expected_petr:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()