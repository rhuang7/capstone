import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for case in range(1, T + 1):
        N = int(input[idx])
        K = int(input[idx + 1])
        idx += 2
        total = (N * (N + 1)) // 2
        power = K
        while power <= N:
            total -= power
            power *= K
        results.append(f"Case #{case}: {total}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()