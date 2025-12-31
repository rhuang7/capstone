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
        
        # The minimum configuration is to have each kid get 1 candy, and then add K to alternate kids
        # To ensure the difference between adjacent kids is at least K, we need to alternate between 1 and 1 + K
        # But since it's a circle, we need to check if this is possible
        # If N is even, it's possible. If N is odd, we need to add an extra K to one of the kids
        if N % 2 == 0:
            total = N + (N // 2) * K
        else:
            total = N + ((N // 2) + 1) * K
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()