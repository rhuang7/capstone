import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            results.append(N)
            continue
        
        # The minimum configuration is to have one kid with 1 candy and the next with 1 + K
        # Then each next kid must be at least K more than the previous
        # This forms an arithmetic sequence with difference K
        # The total is the sum of the arithmetic sequence
        # The sequence starts at 1, then 1 + K, 1 + 2K, ..., 1 + (N-1)K
        # Sum = N * 1 + K * (0 + 1 + 2 + ... + (N-1)) = N + K * (N-1)*N//2
        total = N + K * (N - 1) * N // 2
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()