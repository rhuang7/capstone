import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        # Compute maximum strength
        # The maximum strength is achieved by selecting the largest element
        # and then the next largest, alternating signs
        # So we sort the array and take the largest, then the next largest, etc.
        a_sorted = sorted(a)
        max_strength = 0
        turn = 1  # 1 for +, -1 for -
        for i in range(n-1, -1, -2):
            max_strength += a_sorted[i] * turn
            turn *= -1
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()