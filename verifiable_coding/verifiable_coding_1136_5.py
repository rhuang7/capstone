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
        
        if N % 2 == 0:
            max_sweetness = (N // 2) * K
        else:
            max_sweetness = ((N // 2) + 1) * K
        
        results.append(max_sweetness)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()