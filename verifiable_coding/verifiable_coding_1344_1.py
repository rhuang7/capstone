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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        a.sort()
        min_sum = a[0] + a[1]
        results.append(min_sum)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()