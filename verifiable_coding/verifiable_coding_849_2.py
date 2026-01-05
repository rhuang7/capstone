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

    # Use a dictionary to track the last occurrence of each gcd value
    last_occurrence = {}

    for i in range(n):
        current = arr[i]
        # For each number, we consider it as a subarray of length 1
        # So the gcd is the number itself
        gcd_val = current
        # Update the maximum gcd and length if needed
        if gcd_val > max_gcd:
            max_gcd = gcd_val
            max_len = 1
        elif gcd_val == max_gcd:
            max_len = max(max_len, 1)
        # Update the last occurrence of this gcd value
        last_occurrence[gcd_val] = i

        # Now, for each previous number, compute the gcd with current number
        # and update the last occurrence
        for prev_gcd in list(last_occurrence.keys()):
            new_gcd = math.gcd(prev_gcd, current)
            # Update the last occurrence of new_gcd
            last_occurrence[new_gcd] = i
            # Update the maximum gcd and length if needed
            if new_gcd > max_gcd:
                max_gcd = new_gcd
                max_len = 1
            elif new_gcd == max_gcd:
                max_len = max(max_len, 1)

    print(max_len)

if __name__ == '__main__':
    solve()