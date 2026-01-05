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
        # Because each array of length 1 is valid and contributes 1 to the count
        # For d >= 1, the count is d mod m
        results.append(str(d % m))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()