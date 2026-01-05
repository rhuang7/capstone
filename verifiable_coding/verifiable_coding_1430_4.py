import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx + 1])
        idx += 2
        
        if K == 0:
            results.append(N)
            continue
        
        # The minimum configuration is to have each kid get at least 1 candy,
        # and alternate between 1 and 1 + K to ensure the difference of K.
        # Since it's a circle, the first and last must also differ by at least K.
        # So we need to have at least 1 + K + 1 = K + 2 for the first and last.
        # So the total is N * 1 + (N - 1) * K
        # But if K is 0, we just have N (each gets 1)
        # If K is positive, we need to alternate 1 and 1 + K, which gives total of N + (N - 1) * K
        total = N + (N - 1) * K
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()