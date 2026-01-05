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
        # Compute max strength
        # The maximum alternating sum is achieved by taking the largest element
        # and then the next largest, then the next, etc. So we sort the array
        # and take the maximum possible alternating sum
        a_sorted = sorted(a)
        max_strength = 0
        is_positive = True
        for num in a_sorted:
            if is_positive:
                max_strength += num
            else:
                max_strength -= num
            is_positive = not is_positive
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()