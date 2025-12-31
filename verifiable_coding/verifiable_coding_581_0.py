import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        K = int(data[idx])
        L = int(data[idx+1])
        E = int(data[idx+2])
        idx += 3
        
        ages = list(map(int, data[idx:idx+K]))
        idx += K
        
        total_age = sum(ages) + E
        
        if total_age == 0:
            results.append("NO")
            continue
        
        gcd_val = total_age
        for age in ages:
            gcd_val = gcd(gcd_val, age)
        
        if L % gcd_val == 0:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    solve()