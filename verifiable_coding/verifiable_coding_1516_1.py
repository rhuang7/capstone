import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        if N == 2:
            if K == 1:
                results.append(0)
            else:
                # Unreachable values are 1, 2, ..., K-1
                # But since K >= 2, the first K-1 values are unreachable
                # But since we can make 1 and 2, all values >= 1 can be made
                # So only values < 1 are unreachable, which is 0
                results.append(0)
        else:
            # For N >= 3, the minimal values that can be formed are 1, 2, ..., N-1
            # So all values >= 1 can be formed
            # So the only unreachable values are 0
            results.append(0)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()