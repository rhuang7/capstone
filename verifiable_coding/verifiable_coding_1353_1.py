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
        for _ in range(n):
            t = int(data[idx])
            x1 = int(data[idx+1])
            y1 = int(data[idx+2])
            X1 = int(data[idx+3])
            Y1 = int(data[idx+4])
            idx += 5
            # Check if positions are valid
            if x1 == 1 and X1 == 1 and y1 == Y1:
                results.append("no")
                break
            if x1 == 2 and X1 == 2 and y1 == Y1:
                results.append("no")
                break
            # Check if positions are in same column
            if y1 == Y1:
                results.append("no")
                break
        else:
            results.append("yes")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()