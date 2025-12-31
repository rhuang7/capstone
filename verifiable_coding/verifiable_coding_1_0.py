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
        if (total > 2 * k) or (total < 0) or (k < 0):
            results.append(-1)
            continue
        
        min_moves = (abs(n) + abs(m) + 1) // 2
        if k < min_moves:
            results.append(-1)
            continue
        
        max_diagonal = k - (abs(n) + abs(m) - min_moves)
        if max_diagonal < 0:
            results.append(-1)
            continue
        
        results.append(max_diagonal)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()