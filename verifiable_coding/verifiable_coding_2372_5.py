import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    for n in cases:
        if n == 1:
            print(0)
            continue
        
        # Find the minimum k such that k*(k+1)/2 >= n
        k = math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)
        # Check if k*(k+1)/2 >= n
        while k*(k+1)//2 < n:
            k += 1
        
        # The minimum moves is k + (k - 1)
        print(k + (k - 1))
        
if __name__ == '__main__':
    solve()