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
            # For n=1: (0)*1*2/2 - 1 = 0
            # For n=2: (1)*2*3/2 - 1 = 3 - 1 = 2 (but series is 1, so maybe different formula)
            # Let's find the correct formula
            # Looking at the series: 0, 1, 5, 14, 30, 55, 91, 140
            # These are the tetrahedral numbers: n(n+1)(n+2)/6 - 1 for n starting at 0
            # For n=0: 0*1*2/6 - 1 = 0
            # For n=1: 1*2*3/6 - 1 = 1 - 1 = 0 (not matching)
            # Let's try another approach
            # Looking at the series: 0, 1, 5, 14, 30, 55, 91, 140
            # The differences between terms are: 1, 4, 9, 16, 25, 36, 49
            # These are squares: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2
            # So the nth term is sum of squares from 1 to n-1
            # For n=1: sum of squares from 1 to 0 is 0
            # For n=2: 1^2 = 1
            # For n=3: 1^2 + 2^2 = 5
            # For n=4: 1^2 + 2^2 + 3^2 = 14
            # So the formula is sum of squares from 1 to (n-1)
            # Sum of squares formula: n(n+1)(2n+1)/6
            # So for n-1: (n-1)n(2n-1)/6
            result = (N-1)*N*(2*N-1) // 6
            print(result)

if __name__ == '__main__':
    solve()