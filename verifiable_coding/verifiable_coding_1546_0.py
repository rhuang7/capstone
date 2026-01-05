import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        # Check if it's a valid triangle
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            results.append("NO")
            continue
        # Check if it's a right-angled triangle
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()