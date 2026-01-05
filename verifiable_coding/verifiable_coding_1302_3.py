import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    results = []
    
    for N in cases:
        count = 0
        i = 1
        while i * i <= N:
            if (i * (i + 1)) // 2 <= N:
                count += 1
            i += 1
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()