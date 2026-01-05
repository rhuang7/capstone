import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            results.append(1)
        else:
            # The sequence is based on the pattern of numbers in the form of 6^k - 1
            # For N = 2^k, the value is 6^(k) - 1
            # For other values, it's based on the position in the sequence
            # We can use the formula: value = 6^(k) - 1 where k is the number of times we can divide (N+1) by 2
            k = 0
            temp = N + 1
            while temp % 2 == 0:
                temp //= 2
                k += 1
            value = 6 ** k - 1
            results.append(value)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()