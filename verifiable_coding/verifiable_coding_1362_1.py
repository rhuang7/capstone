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
        # We need to minimize the sum, so we want to flip the sign of the smallest elements
        # However, we must ensure that any contiguous subsequence of length > 1 has a positive sum
        # So we flip the sign of all elements except the smallest one
        # We sort the array, flip all elements except the smallest one
        A_sorted = sorted(A)
        min_val = A_sorted[0]
        for num in A:
            if num != min_val:
                B.append(-num)
            else:
                B.append(num)
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()