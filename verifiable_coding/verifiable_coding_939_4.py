import sys
import math

MOD = 10**9 + 7

def is_lucky(n):
    s = str(n)
    for c in s:
        if c not in {'4', '7'}:
            return False
    return True

def count_lucky_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_lucky(i):
            count += 1
    return count

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        
        # Precompute all lucky numbers up to 10^1000
        # Since 10^1000 has 1001 digits, we can generate all lucky numbers with up to 1001 digits
        # and check if they are in [L, R]
        
        # Generate all lucky numbers
        lucky_numbers = []
        def generate(l, r):
            if l > r:
                return
            lucky_numbers.append(l)
            generate(l * 10 + 4, r)
            generate(l * 10 + 7, r)
        
        generate(4, 10**1000)
        
        # Count how many lucky numbers are in [L, R]
        count = 0
        for num in lucky_numbers:
            if L <= num <= R:
                count += 1
        
        results.append(count % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()