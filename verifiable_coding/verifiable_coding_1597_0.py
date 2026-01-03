import sys
import math

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        M = int(data[index+1])
        index += 2
        possible_N = []
        for N in range(1, M - A + 1):
            if (M - A) % N == 0:
                divisors = get_divisors(N)
                for d in divisors:
                    if A * N + d == M:
                        possible_N.append(N)
                        break
        possible_N = list(set(possible_N))
        possible_N.sort()
        results.append(str(len(possible_N)))
        results.append(' '.join(map(str, possible_N)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()