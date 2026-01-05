import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    cases = list(map(int, input[1:t+1]))
    
    for n in cases:
        if n == 1:
            print(0)
            continue
        
        # Find the minimum k such that k*(k+1)/2 >= n
        k = math.ceil((2 * n)**0.5)
        while k*(k+1)//2 < n:
            k += 1
        
        # The minimum moves is k + (k-1)
        print(k + (k-1))

if __name__ == '__main__':
    solve()