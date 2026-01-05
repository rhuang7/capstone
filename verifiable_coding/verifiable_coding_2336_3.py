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

    # For Petr's method, the number of inversions is roughly O(n^2)
    # For Um_nik's method, the number of inversions is also roughly O(n^2)
    # But since Um_nik's method has more swaps, the number of inversions is more likely to be larger
    # So if inv_count is larger than a certain threshold, it's more likely to be from Um_nik's method
    # We use the fact that Petr's method has 3n swaps and Um_nik's has 7n + 1 swaps
    # So the number of inversions is more likely to be larger for Um_nik's method
    # We use a threshold based on the expected number of inversions for Petr's method
    # Expected number of inversions for Petr's method is roughly 3n^2 / 4
    # So if inv_count is larger than 3n^2 / 4, it's more likely to be from Um_nik's method

    threshold = (3 * n * n) // 4
    if inv_count > threshold:
        print("Um_nik")
    else:
        print("Petr")

if __name__ == '__main__':
    solve()