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

        count0 = s.count('0')
        count1 = s.count('1')

        if count0 != count1:
            print(-1)
            continue

        print(0)

if __name__ == '__main__':
    solve()