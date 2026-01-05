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
        lrs = []
        for _ in range(N):
            l = int(data[idx])
            r = int(data[idx+1])
            lrs.append((l, r))
            idx += 2
        
        # Initialize the power sequences
        power = [0] * N
        for i in range(N):
            power[i] = A[i]
        
        for _ in range(K-1):
            new_power = [0] * N
            for i in range(N):
                l, r = lrs[i]
                xor = 0
                for j in range(l-1, r):
                    xor ^= power[j]
                new_power[i] = xor
            power = new_power
        
        results.append(' '.join(map(str, power)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()