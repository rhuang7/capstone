import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N == 1:
            print(0)
        else:
            # The series is 0, 1, 5, 14, 30, 55, 91, 140...
            # The nth term (starting from 1) is (n-1)*n*(n+1)/2
            # For N=1, it's 0, which is (1-1)*1*(1+1)/2 = 0
            # For N=2, it's (2-1)*2*(2+1)/2 = 3
            # For N=3, it's (3-1)*3*(3+1)/2 = 12
            # But the series is 0, 1, 5, 14, 30, 55, 91, 140...
            # So the formula is (n-1)*n*(n+1)//2
            result = (N-1)*N*(N+1)//2
            print(result)

if __name__ == '__main__':
    solve()