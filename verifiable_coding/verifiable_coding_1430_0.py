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
        
        # The minimum configuration is to have each kid get 1 candy, and then add K to alternate kids
        # So the total is N + K * (N // 2)
        results.append(N + K * (N // 2))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()