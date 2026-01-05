import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    a = int(input[1])
    
    for _ in range(a):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
    print(n)

if __name__ == '__main__':
    solve()