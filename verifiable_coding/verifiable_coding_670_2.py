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
        
        # Sort the array
        A.sort()
        
        # The minimum sum is the sum of the smallest element multiplied by the number of elements
        # because all other elements can be reduced to the smallest element through operations
        min_sum = A[0] * N
        results.append(str(min_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()