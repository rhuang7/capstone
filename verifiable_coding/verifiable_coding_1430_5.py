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
        
        # The minimum configuration is to alternate between 1 and 1 + K
        # Since it's a circle, the first and last elements must also differ by at least K
        # So we need to adjust the sequence to ensure this
        # The minimum total is N + (N - 1) * K
        results.append(N + (N - 1) * K)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()