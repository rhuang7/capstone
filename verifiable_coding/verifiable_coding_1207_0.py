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
        P = list(map(int, data[idx:idx+N]))
        idx += N
        
        P.sort()
        total = 0
        min_p = P[0]
        for i in range(1, N):
            total += min_p * P[i]
            min_p += P[i]
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()