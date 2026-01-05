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
        # The minimal value is (a ^ x) + (b ^ x) for x in [0, 1, ..., 2^30]
        # We can find the optimal x by considering each bit position
        # The minimal value is (a ^ b) << 1
        results.append((a ^ b) << 1)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()