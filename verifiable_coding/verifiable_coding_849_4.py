import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    max_gcd = 0
    max_len = 0

    # Keep track of the current GCDs and their last positions
    gcd_positions = {}

    for i in range(n):
        current = arr[i]
        # For each number, consider it as a subarray starting at i
        # Initialize with the current number
        gcd_positions[current] = i
        # Update GCDs for subarrays ending at i
        for g in list(gcd_positions.keys()):
            new_gcd = math.gcd(g, current)
            if new_gcd in gcd_positions:
                gcd_positions[new_gcd] = i
            else:
                gcd_positions[new_gcd] = i
        # Update max_gcd and max_len
        current_gcd = current
        for g in gcd_positions:
            if g > current_gcd:
                current_gcd = g
        if current_gcd > max_gcd:
            max_gcd = current_gcd
            max_len = 1
        elif current_gcd == max_gcd:
            max_len = 1

    print(max_len)

if __name__ == '__main__':
    solve()