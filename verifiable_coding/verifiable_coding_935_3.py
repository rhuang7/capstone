import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for x in cases:
        if x == 0:
            print(-1)
            continue
        if x % 10 == 0:
            print(0)
            continue
        cnt = 0
        while x % 10 != 0:
            x *= 2
            cnt += 1
            if x > 10**18:
                break
        if x % 10 == 0:
            print(cnt)
        else:
            print(-1)

if __name__ == '__main__':
    solve()