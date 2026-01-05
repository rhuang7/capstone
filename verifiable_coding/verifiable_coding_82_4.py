import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Create a reversed permutation
        p_prime = p[::-1]
        
        # Check if it's the same as original
        if p_prime == p:
            # If it's the same, swap first two elements
            p_prime[0], p_prime[1] = p_prime[1], p_prime[0]
        
        results.append(' '.join(map(str, p_prime)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()