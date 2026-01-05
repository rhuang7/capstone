import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        K = int(input[idx])
        L = int(input[idx+1])
        E = int(input[idx+2])
        idx += 3
        ages = list(map(int, input[idx:idx+K]))
        idx += K
        total_age = sum(ages) + E
        if total_age == 0:
            print("NO")
            continue
        gcd_val = total_age
        for age in ages:
            gcd_val = math.gcd(gcd_val, age)
        if L % gcd_val == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()