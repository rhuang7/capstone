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
        
        if N == 0:
            results.append(0)
            continue
        
        # Maximum sweetness when Chef eats non-adjacent laddus
        # If N is even, he can eat N/2 laddus
        # If N is odd, he can eat (N // 2) + 1 laddus
        max_eaten = (N + 1) // 2
        results.append(max_eaten * K)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()