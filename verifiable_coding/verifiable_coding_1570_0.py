import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        # The maximum number of squares is the sum of squares from 1 to N
        total = sum(x * x for x in range(1, N + 1))
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()