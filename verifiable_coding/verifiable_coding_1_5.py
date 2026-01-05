import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    results = []
    
    for _ in range(q):
        n = int(data[index])
        m = int(data[index+1])
        k = int(data[index+2])
        index += 3
        
        total = n + m
        if total > 2 * k or (total % 2 != k % 2):
            results.append(-1)
            continue
        
        min_diag = max(0, (total - k) // 2)
        max_diag = min(k, (n + m) // 2)
        
        if min_diag > max_diag:
            results.append(-1)
        else:
            results.append(max_diag)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()