import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        if k == 1:
            print(1)
        else:
            pattern = ""
            for i in range(1, k+1):
                if i == 1:
                    pattern += str(i)
                else:
                    pattern += str(i)
            print(pattern)

if __name__ == '__main__':
    solve()