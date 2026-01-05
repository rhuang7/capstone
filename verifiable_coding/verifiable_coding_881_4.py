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
        
        count = 0
        current_length = 1
        
        for i in range(1, N):
            if A[i] >= A[i-1]:
                current_length += 1
            else:
                current_length = 1
            count += current_length
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()