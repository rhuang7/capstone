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
        # We need to ensure that any contiguous subsequence of length > 1 has a positive sum
        # So we flip the sign of the smallest elements, but not all of them
        # We flip the sign of the smallest elements, but only up to the second smallest
        # This ensures that any two consecutive elements have a positive sum
        # We sort the array and flip the sign of the smallest elements
        sorted_A = sorted(A)
        # Flip the sign of the first (N-1) elements
        # Because if we flip the sign of the first (N-1) elements, then any two consecutive elements will have a positive sum
        # The last element remains as is
        for i in range(N-1):
            B.append(-sorted_A[i])
        B.append(sorted_A[-1])
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()