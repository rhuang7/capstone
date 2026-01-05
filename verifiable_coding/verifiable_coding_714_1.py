import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        A = list(map(int, data[index:index + N]))
        index += N
        
        total = sum(A)
        avg = total // N
        
        operations = 0
        for candy in A:
            if candy > avg:
                operations += candy - avg
            elif candy < avg:
                operations += avg - candy
        
        results.append(str(operations))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()