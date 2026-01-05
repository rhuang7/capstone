import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        total = 0
        for k in range(1, N + 1, 2):
            total += (N - k + 1) * (N - k + 2) // 2
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()