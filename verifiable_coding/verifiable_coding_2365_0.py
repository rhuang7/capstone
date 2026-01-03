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
        n = int(data[idx])
        idx += 1
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        # Find the permutation
        # The smallest element in all segments is the first element of the permutation
        # We can use the smallest element as the starting point
        # Then, for each position, we find the next element that is not yet used
        # and is present in the segments that include the current position
        # We can use a greedy approach
        # Start with the smallest element
        used = [False] * (n + 1)
        p = [0] * n
        # Find the smallest element
        min_val = None
        for seg in segments:
            if min_val is None or seg[0] < min_val:
                min_val = seg[0]
        used[min_val] = True
        p[0] = min_val
        # Now find the rest of the permutation
        for i in range(1, n):
            # Find the next element that is not used and is present in any segment that includes the current position
            # We can use the fact that the segments are sorted and the permutation is unique
            # So for each position, the next element is the smallest element in the segments that includes the current position
            # But since we don't know the positions, we can use the fact that the next element must be in the segments
            # and not used yet
            # So we can iterate through all segments and find the smallest element not used
            next_val = None
            for seg in segments:
                for val in seg:
                    if not used[val]:
                        if next_val is None or val < next_val:
                            next_val = val
            used[next_val] = True
            p[i] = next_val
        results.append(' '.join(map(str, p)) + ' ')
    print(''.join(results))

if __name__ == '__main__':
    solve()