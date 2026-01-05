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
        # Let's find the minimal value by considering each bit position
        # The minimal value is achieved when x has bits that minimize the sum
        # The optimal x is such that for each bit, if a and b have the same bit, x should have that bit as 0, otherwise as 1
        # This is equivalent to x = a ^ b
        x = a ^ b
        res = (a ^ x) + (b ^ x)
        results.append(str(res))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()