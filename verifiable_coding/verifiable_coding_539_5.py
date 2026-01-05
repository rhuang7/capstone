import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        # Since M = N + 1, and Bob starts at a corner, the minimum number of moves is (N + 1) * 2 // gcd(N + 1, 4 * N)
        # But since M = N + 1 and the perimeter is 4N, the minimum moves is (N + 1) * 2 // gcd(N + 1, 4 * N)
        # However, since N + 1 and 4N are co-prime when N is even, and have gcd 2 when N is odd
        # So the answer is (N + 1) * 2 // 2 = N + 1 when N is even, and (N + 1) * 2 // 2 = N + 1 when N is odd
        # So the answer is always N + 1
        results.append(str(N + 1))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()