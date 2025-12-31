import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        n = int(data[index+2])
        index += 3
        
        # Compute Xoronacci sequence
        x = [0] * (n + 1)
        x[1] = a
        x[2] = b
        for i in range(3, n + 1):
            x[i] = x[i-1] ^ x[i-2]
        
        # Compute XNoronacci sequence
        e = [0] * (n + 1)
        e[1] = a
        e[2] = b
        for i in range(3, n + 1):
            e[i] = (e[i-1] ^ e[i-2]) ^ 0xFFFFFFFFFFFFFFFF
            e[i] ^= 0xFFFFFFFFFFFFFFFF
        
        print(max(x[n], e[n]))

if __name__ == '__main__':
    solve()