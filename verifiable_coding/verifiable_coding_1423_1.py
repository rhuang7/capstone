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
        K = int(data[idx])
        idx += 1
        
        # Find the value of Uncle Johny
        uncle_johny = A[K-1]
        
        # Sort the list
        sorted_A = sorted(A)
        
        # Find the position of Uncle Johny in the sorted list
        position = sorted_A.index(uncle_johny) + 1
        results.append(str(position))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()