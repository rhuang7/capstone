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

    # Use a dictionary to store the last occurrence of each gcd value
    last_occurrence = {}

    for i in range(n):
        current = arr[i]
        # Initialize the current gcd with the current element
        current_gcd = current
        # Iterate through the previous gcd values
        for g in list(last_occurrence.keys()):
            current_gcd = math.gcd(current_gcd, g)
            if current_gcd == 0:
                break
        # Update the last occurrence of the current_gcd
        last_occurrence[current_gcd] = i
        # Update max_gcd and max_len if needed
        if current_gcd > max_gcd:
            max_gcd = current_gcd
            max_len = 1
        elif current_gcd == max_gcd:
            max_len = max(max_len, i - last_occurrence[current_gcd] + 1)

    print(max_len)

if __name__ == '__main__':
    solve()