import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if N // K == 1:
            results.append("NO")
        else:
            if (N // K) % K == 0:
                results.append("NO")
            else:
                results.append("YES")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()