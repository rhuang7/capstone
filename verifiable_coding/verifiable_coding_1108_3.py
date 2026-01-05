import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    total_minutes = 0
    q_count = 0
    eligible = 0
    
    for _ in range(N):
        total_minutes = 0
        q_count = 0
        for j in range(K):
            total_minutes += int(data[idx])
            idx += 1
        q_count = int(data[idx])
        idx += 1
        
        if total_minutes >= M and q_count <= 10:
            eligible += 1
    
    print(eligible)

if __name__ == '__main__':
    solve()