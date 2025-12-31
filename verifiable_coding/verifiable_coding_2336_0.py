import sys
import random

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    perm = list(map(int, data[1:]))

    # Count the number of inversions
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv += 1

    # Petr's method: 3n swaps
    # Alex's method: 7n + 1 swaps
    # The number of inversions is roughly proportional to the number of swaps
    # So, if inv is small, it's more likely to be Petr's method
    # If inv is large, it's more likely to be Alex's method
    # We use a threshold to decide based on the number of inversions
    if inv < 100000:
        print("Petr")
    else:
        print("Um_nik")

if __name__ == '__main__':
    solve()