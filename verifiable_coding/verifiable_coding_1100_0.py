import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
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
            results.append(0)
            continue
        
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        if diff_p < 0 or diff_q < 0 or diff_r < 0:
            results.append(-1)
            continue
        
        ops = 0
        if diff_p > 0:
            ops += 1
        if diff_q > 0:
            ops += 1
        if diff_r > 0:
            ops += 1
        
        results.append(ops)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()