import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        for __ in range(n):
            t = int(data[idx])
            x1 = int(data[idx+1])
            y1 = int(data[idx+2])
            X1 = int(data[idx+3])
            Y1 = int(data[idx+4])
            idx += 5
            # Check if positions are valid
            # Check if cars are in different lanes
            if x1 == X1:
                results.append("no")
                break
            # Check if positions are valid for the time
            # Check if cars are in different columns
            if y1 == Y1:
                results.append("no")
                break
            # Check if cars are in different rows
            if x1 == 1 and X1 == 2:
                pass
            elif x1 == 2 and X1 == 1:
                pass
            else:
                results.append("no")
                break
        else:
            results.append("yes")
    print('\n'.join(results))