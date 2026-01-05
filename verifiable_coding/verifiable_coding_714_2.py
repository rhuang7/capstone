import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = sum(A)
        avg = total // N
        
        operations = 0
        for num in A:
            if num > avg:
                operations += num - avg
            elif num < avg:
                operations += avg - num
        
        results.append(str(operations))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()