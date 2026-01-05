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
        # Initialize the current power of the sequence
        current = A.copy()
        # If K is 1, output the original sequence
        if K == 1:
            results.append(' '.join(map(str, current)))
            continue
        # For K > 1, compute the power iteratively
        for _ in range(K-1):
            next_power = [0] * N
            for i in range(N):
                li = l[i] - 1
                ri = r[i] - 1
                # Compute XOR of current[li ... ri]
                xor = 0
                for j in range(li, ri + 1):
                    xor ^= current[j]
                next_power[i] = xor
            current = next_power
        results.append(' '.join(map(str, current)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()