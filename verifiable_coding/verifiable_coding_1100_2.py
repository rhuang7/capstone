import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        p = int(data[index])
        q = int(data[index+1])
        r = int(data[index+2])
        index += 3
        
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        if (p == a and q == b and r == c):
            print(0)
            continue
        
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        if (diff_p < 0 or diff_q < 0 or diff_r < 0):
            print(-1)
            continue
        
        if (diff_p == 0 and diff_q == 0 and diff_r == 0):
            print(0)
            continue
        
        max_ops = 0
        if diff_p > 0:
            max_ops += 1
        if diff_q > 0:
            max_ops += 1
        if diff_r > 0:
            max_ops += 1
        
        print(max_ops)
        
if __name__ == '__main__':
    solve()