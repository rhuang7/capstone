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
        # Check if the sides can form a triangle
        a, b, c = sorted([A, B, C])
        if a + b <= c:
            results.append("NO")
        else:
            # Check if it's a right-angled triangle
            if a*a + b*b == c*c:
                results.append("YES")
            else:
                results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()