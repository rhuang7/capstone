import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        # The minimal value is (a ^ x) + (b ^ x)
        # We can simplify this expression
        # (a ^ x) + (b ^ x) = (a + b) - 2 * (a & b) if x is a common bit pattern
        # But the minimal value occurs when x is the bitwise AND of a and b
        # So the minimal value is (a ^ (a & b)) + (b ^ (a & b))
        # Which simplifies to (a | b) - (a & b)
        min_val = (a | b) - (a & b)
        results.append(str(min_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()