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

    # Use a dictionary to keep track of the last occurrence of each GCD
    last_occurrence = {}

    for i in range(n):
        current = arr[i]
        # For each element, we consider all possible GCDs that can be formed with this element
        # Start with the element itself
        temp_gcd = current
        # Update the last occurrence of this GCD
        last_occurrence[temp_gcd] = i
        # Now check with previous elements to find possible GCDs
        for j in range(i - 1, -1, -1):
            temp_gcd = math.gcd(temp_gcd, arr[j])
            # Update the last occurrence of this GCD
            last_occurrence[temp_gcd] = j
            # If this GCD has been seen before, we can update the max_len
            if temp_gcd in last_occurrence:
                current_len = i - last_occurrence[temp_gcd] + 1
                if current_len > max_len:
                    max_len = current_len
                    max_gcd = temp_gcd
            else:
                # If not seen before, we can't update the max_len
                pass

    print(max_len)

if __name__ == '__main__':
    solve()