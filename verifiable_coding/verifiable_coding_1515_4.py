import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        if not s:
            continue
        first_char = s[0]
        if first_char == 'a':
            base = 100
        elif first_char == 'z':
            base = 2600
        else:
            base = 100 + (ord(first_char) - ord('a')) * 100
        
        total = 0
        for c in s:
            val = base + (ord(c) - ord('a'))
            total += val
            total %= MOD
        
        print(total % MOD)

if __name__ == '__main__':
    solve()