import sys
import random

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Calculate the number of inversions
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1

    # Petr's method: 3n swaps
    # Alex's method: 7n + 1 swaps
    # The number of inversions is roughly proportional to the number of swaps
    # So, if the number of inversions is small, it's more likely to be Petr's method
    # If it's larger, it's more likely to be Alex's method
    # We can use a threshold to decide
    if inversions < 2 * n:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()