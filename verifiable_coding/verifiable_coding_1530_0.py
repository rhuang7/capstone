import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for K in cases:
        if K == 1:
            print(1)
        else:
            pattern = ""
            for i in range(1, K+1):
                pattern += str(i)
            for i in range(K-1, 0, -1):
                pattern += str(i)
            print(pattern)

if __name__ == '__main__':
    solve()