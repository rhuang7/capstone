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
        # Initialize the current gcd with the current element
        current_gcd = current
        # For each previous element, compute the gcd with current element
        for j in range(i, -1, -1):
            current_gcd = math.gcd(current_gcd, arr[j])
            # If this gcd has been seen before, update the last occurrence
            if current_gcd in last_occurrence:
                last_occurrence[current_gcd] = i
            else:
                last_occurrence[current_gcd] = i
            # Update max_gcd and max_len
            if current_gcd > max_gcd:
                max_gcd = current_gcd
                max_len = i - j + 1
            elif current_gcd == max_gcd:
                max_len = max(max_len, i - j + 1)

    print(max_len)

if __name__ == '__main__':
    solve()