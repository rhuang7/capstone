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
            # The pattern is (n-1)*n*(n+1)/2 - 1
            result = (N-1)*N*(N+1)//2 - 1
            print(result)

if __name__ == '__main__':
    solve()