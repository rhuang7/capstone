import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for N in cases:
        if int(N) % 9 == 0:
            print(0)
            continue
        s = list(N)
        total = 0
        for i in range(len(s)):
            d = int(s[i])
            if d > 9:
                d = 9
            if d < 0:
                d = 0
            total += abs(d - 9)
        print(total)

if __name__ == '__main__':
    solve()