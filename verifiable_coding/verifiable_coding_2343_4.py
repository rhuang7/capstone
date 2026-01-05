import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        d = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        # The answer is the sum of all numbers from 1 to d, modulo m
        # Because for each a_1, a_2, ..., a_n, the sequence b is strictly increasing
        # and the only valid sequences are those where each element is strictly increasing
        # and the XOR of the previous elements is less than the current element
        # This is equivalent to counting the number of strictly increasing sequences
        # of length >= 1, which is the sum of all numbers from 1 to d
        res = sum(range(1, d+1)) % m
        results.append(res)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()