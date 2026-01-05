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
        # For each element, compute gcd with all previous gcd values
        # Start with the current element itself
        temp = {}
        temp[current] = i
        # Check previous gcd values
        for g in last_occurrence:
            new_gcd = math.gcd(g, current)
            if new_gcd in temp:
                temp[new_gcd] = max(temp[new_gcd], last_occurrence[g])
            else:
                temp[new_gcd] = last_occurrence[g]
        # Update the last_occurrence with the new gcd values
        last_occurrence = temp
        # Update max_gcd and max_len
        for g in last_occurrence:
            if g > max_gcd:
                max_gcd = g
                max_len = last_occurrence[g] - i + 1
            elif g == max_gcd:
                max_len = max(max_len, last_occurrence[g] - i + 1)

    print(max_len)

if __name__ == '__main__':
    solve()