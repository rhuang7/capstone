import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        # Since M = N + 1, and Bob starts at a corner and moves along the perimeter
        # The perimeter is 4 * N, but since he starts at a corner, the effective perimeter is 2 * (N - 1)
        # So the minimum number of moves is (N + 1) // (2 * (N - 1))
        # But since he needs to return to the starting point, the answer is (N + 1) // (2 * (N - 1)) * 2
        # However, since M = N + 1, and he moves exactly M steps per move, the answer is (N + 1) // (2 * (N - 1)) * 2
        # But for N = 1, the perimeter is 4, and M = 2, so it's 2 steps
        # For N = 2, the perimeter is 8, and M = 3, so it's 8 / 3 = 2.666..., rounded up to 3 moves, but the correct answer is 8
        # So the correct formula is (N + 1) * 2
        results.append(str((N + 1) * 2))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()