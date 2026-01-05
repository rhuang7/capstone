import sys
import math

def count_ones(x):
    return bin(x).count('1')

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = list(map(int, data[idx:idx+Q]))
        idx += Q
        even = 0
        odd = 0
        for num in A:
            cnt = count_ones(num)
            if cnt % 2 == 0:
                even += 1
            else:
                odd += 1
        for P in queries:
            even_count = 0
            odd_count = 0
            for num in A:
                x = P ^ num
                cnt = count_ones(x)
                if cnt % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            results.append(f"{even_count} {odd_count}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()