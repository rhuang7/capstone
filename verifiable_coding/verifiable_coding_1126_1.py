import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for n in cases:
        if n == 0:
            print(1)
        else:
            print(2 * n * (n + 1) // 2 - n + 1)
            
if __name__ == '__main__':
    solve()