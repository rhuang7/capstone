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
        
        # Minimum configuration: start with 1, then add K each time
        # But since it's a circle, the last and first must also differ by at least K
        # So we need to adjust the sequence to ensure this
        # The minimum sequence is 1, 1 + K, 1 + 2K, ..., 1 + (N-1)K
        # But the last and first must differ by at least K
        # So we need to add K to the last element to ensure this
        # Total = sum(1 + i*K for i in range(N)) + K
        total = sum(1 + i * K for i in range(N)) + K
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()