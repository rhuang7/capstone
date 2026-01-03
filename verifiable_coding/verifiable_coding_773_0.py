import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for n in cases:
        if n == 2:
            print("2 1")
        else:
            res = []
            for i in range(1, n+1):
                if i % 2 == 1:
                    res.append(i+1)
                else:
                    res.append(i-1)
            print(' '.join(map(str, res)))
    
if __name__ == '__main__':
    solve()