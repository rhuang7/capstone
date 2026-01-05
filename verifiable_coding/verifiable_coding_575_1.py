import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        n = len(s)
        if n == 0:
            print(1)
            continue
        # Initialize variables to track the minimum and maximum values needed
        min_val = 1
        max_val = 1
        prev = 1
        for c in s:
            if c == '<':
                # Need to increase the value
                if prev < min_val:
                    min_val = prev + 1
                prev = min_val
                max_val = prev
            elif c == '>':
                # Need to decrease the value
                if prev > max_val:
                    max_val = prev - 1
                prev = max_val
                min_val = prev
            else:  # '='
                # Value remains the same
                prev = min_val
                max_val = prev
        print(max_val)

if __name__ == '__main__':
    solve()