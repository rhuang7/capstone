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
            if A[i] == min(A):
                target = A[i]
                break
        
        for i in range(N):
            if A[i] != target:
                moves = 0
                current = A[i]
                while current != target:
                    current = A[i-1] if i > 0 else A[i+1]
                    moves += 1
                min_moves = min(min_moves, moves)
        
        results.append(min_moves)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()