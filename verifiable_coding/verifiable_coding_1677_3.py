import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    b = list(map(int, data[N+1:2*N+1]))
    
    max_sum = -float('inf')
    
    for i in range(N):
        current_sum = a[i] + b[i]
        max_sum = max(max_sum, current_sum)
        for j in range(i+1, N):
            current_sum += b[j]
            max_sum = max(max_sum, current_sum)
    
    for i in range(N):
        current_sum = a[i] + b[i]
        max_sum = max(max_sum, current_sum)
        for j in range(i+1, N):
            current_sum += b[j]
            max_sum = max(max_sum, current_sum)
    
    print(max_sum)

if __name__ == '__main__':
    solve()