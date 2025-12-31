import sys

def largest_prime_factor(n):
    if n == 1:
        return 1
    largest = -1
    while n % 2 == 0:
        largest = 2
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 2
    if n > 1:
        largest = n
    return largest

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        lpf_list = []
        for num in A:
            lpf = largest_prime_factor(num)
            lpf_list.append(lpf)
        max_count = -1
        result = -1
        for lp in lpf_list:
            if lpf_list.count(lp) > max_count:
                max_count = lpf_list.count(lp)
                result = lp
            elif lpf_list.count(lp) == max_count and lp > result:
                result = lp
        results.append(str(result))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()