import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        K = int(data[i])
        pos = 1
        while K > 1:
            K = (K + 1) // 2
            pos *= 2
        results.append(str(pos))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()