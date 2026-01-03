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
        # But the minimal value is achieved when x is a common bit pattern
        # So the minimal value is (a + b) - 2 * (a & b)
        # But this is only true when x is such that it sets the bits where a and b differ to 0
        # So the minimal value is (a ^ b) + 2 * (a & b) - 2 * (a & b) = a ^ b
        # Wait, no, let's think again
        # Let's find the minimal value of (a ^ x) + (b ^ x)
        # Let's consider the binary representation of a and b
        # For each bit position, if a and b have the same bit, then x can be set to 0, and the contribution to the sum is 0
        # If a and b have different bits, then x can be set to 1, and the contribution to the sum is 2 (since 1 ^ 1 = 0, 0 ^ 1 = 1, so 1 + 1 = 2)
        # So the minimal value is the number of differing bits between a and b multiplied by 2
        # So the minimal value is (a ^ b).bit_count() * 2
        min_val = (a ^ b).bit_count() * 2
        results.append(str(min_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()