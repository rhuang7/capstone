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
        d = int(data[idx+3])
        idx += 4
        # Mr. Pr's position after t seconds: a + c * x + d * y
        # Ms. Ad's position after t seconds: b + d * x + c * y
        # They meet when a + c * x + d * y = b + d * x + c * y
        # Rearranging: a - b = (d - c) * x - (c - d) * y
        # Simplify: a - b = (d - c)(x - y)
        # Let t = x + y, then x - y = k, and x = (t + k)/2, y = (t - k)/2
        # So a - b must be divisible by (d - c)
        # Also, t must be such that x and y are non-negative integers
        # So, check if (a - b) is divisible by (d - c)
        # Also, check if there exists t such that x and y are non-negative integers
        if d == c:
            # If c == d, then both move same distance per second, so they can only meet if a == b
            if a == b:
                results.append("YES")
            else:
                results.append("NO")
            continue
        diff = a - b
        if diff % (d - c) != 0:
            results.append("NO")
            continue
        # Check if there exists t such that x and y are non-negative integers
        # Let k = (a - b) / (d - c)
        # Then x - y = k
        # Also, x + y = t
        # So x = (t + k)/2, y = (t - k)/2
        # Both x and y must be non-negative integers
        # So t must be >= |k| and t must have the same parity as |k|
        # So, check if there exists t >= |k| such that t and |k| have same parity
        k = diff // (d - c)
        if k < 0:
            k = -k
        if k % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()