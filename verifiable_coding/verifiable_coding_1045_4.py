import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        res = 0
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u'}:
                res = (res * 2 + 0) % MOD
            else:
                res = (res * 2 + 1) % MOD
        print(res)

if __name__ == '__main__':
    solve()