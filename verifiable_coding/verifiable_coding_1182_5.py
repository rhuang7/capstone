import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ms = list(map(int, data[1:T+1]))
    
    results = []
    
    for M in Ms:
        if M == 1:
            results.append("1\n1")
            continue
        
        divisors = []
        for i in range(1, int(math.isqrt(M)) + 1):
            if M % i == 0:
                divisors.append(i)
                if i != M // i:
                    divisors.append(M // i)
        divisors = list(set(divisors))
        divisors.sort()
        
        interesting = set()
        for d in divisors:
            a = d
            b = (a * d) // M
            if a * b % M == 0 and (a * b) // M == a + b:
                interesting.add(a)
        
        interesting = sorted(interesting)
        K = len(interesting)
        results.append(f"{K}\n{'\n'.join(map(str, interesting))}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()