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
        curr = A.copy()
        # For each step from 2 to K
        for _ in range(K-1):
            # Compute the next power using XOR of ranges
            next_power = [0]*N
            for i in range(N):
                li = l[i]-1
                ri = r[i]-1
                # Compute XOR of curr[li ... ri]
                xor = 0
                for j in range(li, ri+1):
                    xor ^= curr[j]
                next_power[i] = xor
            curr = next_power
        results.append(' '.join(map(str, curr)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()