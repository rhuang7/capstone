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
        # Process each query
        for P in queries:
            # XOR each element with P and count 1s
            even_cnt = 0
            odd_cnt = 0
            for num in A:
                xor_val = num ^ P
                cnt = count_ones(xor_val)
                if cnt % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
            results.append(f"{even_cnt} {odd_cnt}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()