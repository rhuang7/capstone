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
        
        even = 0
        odd = 0
        
        for num in A:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        result = even * odd
        results.append(str(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()