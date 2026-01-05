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
        
        # Sort the array in descending order
        A.sort(reverse=True)
        
        # Chef takes first, then Roma, and so on
        # Total stones Chef can take is sum of every other element starting from index 0
        total_chef = sum(A[i] for i in range(0, N, 2))
        results.append(str(total_chef))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()