import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        seen = set()
        res = 0
        
        from itertools import permutations
        
        for perm in permutations(s):
            num_str = ''.join(perm)
            if num_str[0] == '0':
                continue
            num = int(num_str)
            if num & (num - 1) == 0:  # Check if it's a power of two
                if num not in seen:
                    seen.add(num)
                    res = (res + num) % MOD
        
        if res == 0:
            print(-1)
        else:
            print(res)

if __name__ == '__main__':
    solve()