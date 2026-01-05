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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_len = 1
        for i in range(2, N):
            if arr[i] == arr[i-1] + arr[i-2]:
                max_len = max(max_len, i - 1 + 1)
            else:
                max_len = 1
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()