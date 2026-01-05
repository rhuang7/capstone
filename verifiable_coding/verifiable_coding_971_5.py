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
        
        if len(set(A)) == 1:
            results.append(0)
            continue
        
        min_moves = float('inf')
        target = None
        
        for i in range(N):
            if A[i] != A[0]:
                target = A[i]
                break
        
        if target is None:
            target = A[-1]
        
        moves = 0
        for i in range(N):
            if A[i] != target:
                moves += 1
        
        results.append(moves)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()