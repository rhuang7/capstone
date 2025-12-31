import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        n = len(s)
        if n % 2 != 0:
            print(-1)
            continue
        count_0 = s.count('0')
        count_1 = s.count('1')
        if count_0 != count_1:
            print(-1)
            continue
        print(0)

if __name__ == '__main__':
    solve()