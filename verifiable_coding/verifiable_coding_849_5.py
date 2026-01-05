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

    # Use a dictionary to keep track of the last occurrence of each gcd value
    last_occurrence = {}

    for i in range(n):
        current = arr[i]
        # For each element, we consider all possible gcds with previous elements
        # Start with the current element itself
        temp = {current: i}
        for j in range(i-1, -1, -1):
            # Compute gcd of current element and the previous element
            gcd_val = math.gcd(arr[j], current)
            # Update the temp dictionary with the new gcd value
            temp[gcd_val] = j
            # If the gcd value is already in the dictionary, we keep the last occurrence
            if gcd_val in last_occurrence:
                last_occurrence[gcd_val] = j
            else:
                last_occurrence[gcd_val] = j
        # Update the maximum gcd and its length
        current_gcd = max(temp.keys())
        if current_gcd > max_gcd:
            max_gcd = current_gcd
            max_len = 1
        elif current_gcd == max_gcd:
            max_len = max(max_len, i - last_occurrence[current_gcd] + 1)

    print(max_len)

if __name__ == '__main__':
    solve()