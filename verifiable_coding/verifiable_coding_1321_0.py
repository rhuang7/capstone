import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            results.append('0')
        else:
            # The series is 0, 1, 5, 14, 30, 55, 91, 140...
            # The pattern is (n-1)*n*(n+1)/2 - 1
            # For n=1: (0*1*2)/2 - 1 = 0 - 1 = -1 (but we use 0)
            # For n=2: (1*2*3)/2 - 1 = 3 - 1 = 2 (but we use 1)
            # So the formula is (n-1)*n*(n+1)//2 - 1 for n >= 2
            res = ( (N-1)*N*(N+1) ) // 2 - 1
            results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()