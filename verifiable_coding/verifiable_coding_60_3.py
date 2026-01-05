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
        # Let's find the minimal value by considering the binary representation
        # The minimal value is (a ^ b) + 2 * (a & b)
        # Because (a ^ x) + (b ^ x) = (a ^ b) + 2 * (a & b)
        res = (a ^ b) + 2 * (a & b)
        results.append(res)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()