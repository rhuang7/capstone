import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        # The minimal value is (a ^ x) + (b ^ x)
        # Let's find the minimal value by considering the binary representation
        # The minimal value is (a ^ b) if a and b have different bits
        # Otherwise, it's (a ^ b) + 2^k for some k
        # But the minimal value is (a ^ b) if a and b have different bits
        # Wait, let's think differently:
        # (a ^ x) + (b ^ x) = (a ^ b) + 2 * (x ^ (a & b))
        # So to minimize this, we need to minimize (x ^ (a & b))
        # The minimal value of (x ^ (a & b)) is 0, so the minimal value is (a ^ b)
        # So the answer is (a ^ b)
        results.append(str(a ^ b))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()