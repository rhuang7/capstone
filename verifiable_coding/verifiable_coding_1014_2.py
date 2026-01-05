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
        total = 0
        
        from itertools import permutations
        
        for perm in permutations(s):
            if perm[0] == '0':
                continue
            num = int(''.join(perm))
            if num in seen:
                continue
            seen.add(num)
            if (num & (num - 1)) == 0:  # Check if it's a power of two
                total += num
        
        if total == 0:
            print(-1)
        else:
            print(total % MOD)

if __name__ == '__main__':
    solve()