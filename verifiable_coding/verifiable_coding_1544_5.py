import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print("*")
        else:
            for i in range(1, k+1):
                if i % 2 == 1:
                    print("*" * i)
                else:
                    print("*" * (i//2) + " " * (i - i//2) + "*" * (i//2))
                    
if __name__ == '__main__':
    solve()