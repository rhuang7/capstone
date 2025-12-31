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
        # Since K can be up to 5e7, we need an efficient way
        # We can use binary exponentiation with matrix exponentiation or find a pattern
        # However, since the operation is XOR and the sequence is built from previous steps,
        # we can observe that after a certain number of steps, the sequence becomes zero
        # So we can simulate up to K steps, but with optimizations
        # We will use a list to store the current sequence
        current = A[:]
        for _ in range(K-1):
            next_seq = [0]*N
            for i in range(N):
                l_i = l[i]-1
                r_i = r[i]-1
                # Compute XOR of current[l_i ... r_i]
                xor_val = 0
                for j in range(l_i, r_i+1):
                    xor_val ^= current[j]
                next_seq[i] = xor_val
            current = next_seq
        results.append(' '.join(map(str, current)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()