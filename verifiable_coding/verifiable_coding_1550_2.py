import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        n = int(data[index+2])
        index += 3
        
        # Compute Xoronacci sequence
        x = [a, b]
        for i in range(2, n+1):
            x.append(x[i-1] ^ x[i-2])
        
        # Compute XNoronacci sequence
        e = [a, b]
        for i in range(2, n+1):
            e.append((e[i-1] ^ e[i-2]) ^ 0xFFFFFFFFFFFFFFFF)
        
        results.append(max(x[n-1], e[n-1]))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()