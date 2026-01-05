import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    K = int(data[idx+2])
    idx += 3
    
    count = 0
    
    for _ in range(N):
        total_time = 0
        Q = 0
        for j in range(K):
            total_time += int(data[idx])
            idx += 1
        Q = int(data[idx])
        idx += 1
        
        if total_time >= M and Q <= 10:
            count += 1
    
    print(count)

if __name__ == '__main__':
    solve()