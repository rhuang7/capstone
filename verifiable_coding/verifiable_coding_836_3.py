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
        n = int(data[idx])
        idx += 1
        L = list(map(int, data[idx:idx+n]))
        idx += n
        R = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_lr = -1
        max_r = -1
        best_index = -1
        
        for i in range(n):
            lr = L[i] * R[i]
            if lr > max_lr or (lr == max_lr and R[i] > max_r) or (lr == max_lr and R[i] == max_r and i < best_index):
                max_lr = lr
                max_r = R[i]
                best_index = i + 1  # 1-based index
        
        results.append(str(best_index))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()