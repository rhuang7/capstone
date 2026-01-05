import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Compute the number of inversions
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1

    # Petr's method has about 3n swaps, which leads to about 3n^2 / 4 inversions
    # Alex's method has about 7n+1 swaps, which leads to about (7n+1)^2 / 4 inversions
    # We can approximate the number of inversions to decide which method was used

    # Use the approximate formula for the number of inversions after k swaps
    # The expected number of inversions after k swaps is roughly k * (n - 1) / 2
    # But since we don't know k, we can use the approximate formula based on the number of inversions

    # Petr's method: expected inversions ~ 3n^2 / 4
    # Alex's method: expected inversions ~ (7n)^2 / 4

    petr_inv = 3 * n * n // 4
    umnik_inv = (7 * n) * (7 * n) // 4

    if inversions < petr_inv:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()