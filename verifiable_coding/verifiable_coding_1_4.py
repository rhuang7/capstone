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
        
        # Total steps required to reach (n, m) in minimum steps
        min_steps = max(n, m)
        if min_steps > k:
            results.append(-1)
            continue
        
        # Remaining steps after minimum steps
        remaining = k - min_steps
        
        # Check if remaining steps are even
        if remaining % 2 != 0:
            results.append(-1)
            continue
        
        # Maximum diagonal moves is (min_steps - remaining // 2)
        max_diagonal = min_steps - (remaining // 2)
        results.append(max_diagonal)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()