import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        # Check if they can form a triangle
        sides = sorted([A, B, C])
        if sides[0] + sides[1] <= sides[2]:
            results.append("NO")
        else:
            # Check if it's a right-angled triangle
            if sides[0]**2 + sides[1]**2 == sides[2]**2:
                results.append("YES")
            else:
                results.append("NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()