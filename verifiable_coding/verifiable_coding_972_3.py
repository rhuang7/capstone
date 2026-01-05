import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    h = list(map(int, data[2:]))
    
    h.sort()
    
    min_diff = float('inf')
    
    for i in range(N - K + 1):
        current_diff = h[i + K - 1] - h[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    print(min_diff)

if __name__ == '__main__':
    solve()