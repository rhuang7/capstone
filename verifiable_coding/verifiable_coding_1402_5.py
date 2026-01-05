import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        A = data[idx]
        idx += 1
        B = data[idx]
        idx += 1
        
        a = int(A, 2)
        b = int(B, 2)
        count = 0
        
        while b > 0:
            u = a ^ b
            v = (a & b) << 1
            a = u
            b = v
            count += 1
        
        print(count)

if __name__ == '__main__':
    solve()