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
        # The maximum strength is achieved by selecting the largest element, then the second largest, etc.
        # But since the alternating sum is + - + -, we want to select the largest element, then the second smallest, etc.
        # So we sort the array and take the largest, then the smallest, then the next largest, etc.
        a.sort()
        max_strength = 0
        is_positive = True
        for i in range(n):
            if is_positive:
                max_strength += a[i]
            else:
                max_strength -= a[i]
            is_positive = not is_positive
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()