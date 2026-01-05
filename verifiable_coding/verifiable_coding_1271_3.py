import sys

def count_bits(x):
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
        Q = int(data[idx])
        idx += 1
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        S = set()
        for x in queries:
            new_elements = set()
            for y in S:
                new_elements.add(y ^ x)
            new_elements.add(x)
            for e in new_elements:
                if e not in S:
                    S.add(e)
            even = 0
            odd = 0
            for num in S:
                if count_bits(num) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            results.append(f"{even} {odd}")
    print('\n'.join(results))