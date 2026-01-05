import sys
import random

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Count the number of inversions
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1

    # Petr's method: 3n swaps
    # Alex's method: 7n + 1 swaps
    # More swaps generally mean more inversions
    # But we need to determine which method is more likely to produce the given permutation

    # For Petr's method, the expected number of inversions is roughly n^2 / 4
    # For Alex's method, the expected number of inversions is roughly (7n + 1) * n / 2
    # But we can't compute exact expected values, so we use the number of inversions to decide

    # If the number of inversions is small, it's more likely to be from Petr's method
    # If the number of inversions is large, it's more likely to be from Alex's method

    # Use a threshold to decide
    if inversions < n * n // 4:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()