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
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        # Precompute the count of 1s for each element in A
        even = 0
        odd = 0
        for num in A:
            cnt = count_ones(num)
            if cnt % 2 == 0:
                even += 1
            else:
                odd += 1
        # Process queries
        for P in queries:
            # XOR each element with P and count 1s
            even_query = 0
            odd_query = 0
            for num in A:
                x = num ^ P
                cnt = count_ones(x)
                if cnt % 2 == 0:
                    even_query += 1
                else:
                    odd_query += 1
            results.append(f"{even_query} {odd_query}")
    print('\n'.join(results))