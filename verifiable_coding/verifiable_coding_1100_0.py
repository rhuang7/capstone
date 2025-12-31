import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        p = int(data[idx])
        q = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # Check if the target is achievable
        if (a - p) < 0 or (b - q) < 0 or (c - r) < 0:
            results.append("-1")
            continue
        
        # Calculate the differences
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        # Check if all differences are zero
        if diff_p == 0 and diff_q == 0 and diff_r == 0:
            results.append("0")
            continue
        
        # Count the number of non-zero differences
        non_zero = 0
        if diff_p != 0:
            non_zero += 1
        if diff_q != 0:
            non_zero += 1
        if diff_r != 0:
            non_zero += 1
        
        # Maximum number of operations is the number of non-zero differences
        results.append(str(non_zero))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()