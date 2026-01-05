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
        
        if N == 0:
            results.append(0)
            continue
        
        # Maximum sweetness when Chef eats non-adjacent laddus
        # Chef can eat at most ceil(N / 2) laddus
        max_laddus = (N + 1) // 2
        max_sweetness = max_laddus * K
        results.append(max_sweetness)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()