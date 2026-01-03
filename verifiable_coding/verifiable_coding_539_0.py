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
        # But since M = N + 1 and the perimeter is 4N, the minimum moves is (4N) // gcd(N + 1, 4N)
        # But since N + 1 and 4N are coprime, the answer is 4N // (N + 1)
        # However, since Bob can't reverse direction and must return to the start, the correct formula is (N + 1) * 2 // gcd(N + 1, 4 * N)
        # But since N + 1 and 4N are coprime, the answer is (N + 1) * 2 // (N + 1) = 2
        # Wait, this is not correct. Let's re-calculate.
        # The perimeter is 4N. Bob takes M = N + 1 steps per move.
        # The number of moves required to return is (4N) // gcd(N + 1, 4N)
        # Since gcd(N + 1, 4N) = gcd(N + 1, 4)
        # So the answer is (4N) // gcd(N + 1, 4)
        # For N = 1, gcd(2, 4) = 2, so 4*1 // 2 = 2
        # For N = 2, gcd(3, 4) = 1, so 4*2 // 1 = 8
        # So the correct formula is (4 * N) // gcd(N + 1, 4)
        # Compute gcd
        from math import gcd
        g = gcd(N + 1, 4)
        res = (4 * N) // g
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()