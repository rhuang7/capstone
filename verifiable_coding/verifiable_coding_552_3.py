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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        W = list(map(int, data[idx:idx+N]))
        idx += N
        
        W.sort()
        total = sum(W)
        sum_k = sum(W[-K:])
        sum_rest = total - sum_k
        difference = sum_rest - sum_k
        results.append(str(difference))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()