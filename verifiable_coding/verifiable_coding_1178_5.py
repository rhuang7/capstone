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
        
        A.sort()
        count = 0
        for a in A:
            if count < a:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()