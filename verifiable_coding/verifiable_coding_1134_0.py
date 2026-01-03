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
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        current_army = 0
        defeated = False
        
        for i in range(N):
            if i < M:
                current_army += A[i]
            else:
                loss = (A[i] + 1) // 2
                current_army -= loss
                if current_army <= 0:
                    defeated = True
                    break
        
        if defeated:
            results.append("DEFEAT")
        else:
            results.append("VICTORY")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()