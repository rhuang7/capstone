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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        l = []
        r = []
        for _ in range(N):
            li = int(data[idx])
            ri = int(data[idx+1])
            l.append(li)
            r.append(ri)
            idx += 2
        # Compute A^K
        # Use binary exponentiation
        # Since K can be up to 5e7, we need an efficient way
        # We will represent the current sequence as a list of integers
        # For each step, we compute the next sequence using the given operation
        # Since the operation is XOR over a range, we can precompute prefix XORs
        # to make the range XOR queries efficient
        # Precompute prefix XORs
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] ^ A[i]
        # Function to compute XOR of range [l, r]
        def range_xor(l, r):
            return prefix[r] ^ prefix[l-1]
        # Binary exponentiation
        # Initialize the result as the original sequence
        current = A[:]
        for _ in range(K-1):
            next_seq = [0] * N
            for i in range(N):
                li = l[i]
                ri = r[i]
                next_seq[i] = range_xor(li, ri)
            current = next_seq
        results.append(' '.join(map(str, current)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()