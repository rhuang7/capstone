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
        # Precompute even and odd counts for each element in A
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
            # XOR with P will flip bits, but the parity of the number of 1s remains the same
            # So the counts of even and odd remain the same
            results.append(f"{even} {odd}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()