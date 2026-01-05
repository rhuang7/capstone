import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for N in cases:
        s = N
        n = len(s)
        result = 0
        power = 1
        for i in range(n):
            shift = s[i:] + s[:i]
            num = int(shift)
            result = (result + num * power) % MOD
            power = (power * 10**n) % MOD
        print(result)
        
if __name__ == '__main__':
    solve()