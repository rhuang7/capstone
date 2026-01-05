import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = []
        # We will flip the sign of the smallest elements to minimize the sum
        # but ensure that any contiguous subsequence of length > 1 has positive sum
        # So we sort the array and flip the sign of the smallest elements
        # but keep at least one positive element to avoid all negatives
        A_sorted = sorted(A)
        flipped = 0
        for i in range(N):
            if flipped < N - 1 and A_sorted[i] < 0:
                B.append(-A_sorted[i])
                flipped += 1
            else:
                B.append(A_sorted[i])
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()