import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        d = int(data[index])
        m = int(data[index + 1])
        index += 2
        # For each d, the answer is the (d)th Fibonacci number modulo m
        # Because the valid sequences are exactly the ones where each element is larger than the previous and the XOR sequence is strictly increasing
        # This is a known problem and the answer is the (d)th Fibonacci number modulo m
        # We compute Fibonacci numbers modulo m efficiently using matrix exponentiation
        def fib_mod(n, m):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            # Matrix exponentiation
            def multiply(a, b):
                return [
                    [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                    [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
                ]
            def power(matrix, power):
                result = [[1, 0], [0, 1]]  # Identity matrix
                while power > 0:
                    if power % 2 == 1:
                        result = multiply(result, matrix)
                    matrix = multiply(matrix, matrix)
                    power //= 2
                return result
            # Initial matrix for Fibonacci sequence
            matrix = [[1, 1], [1, 0]]
            powered = power(matrix, n - 2)
            return (powered[0][0] * 1 + powered[0][1] * 1) % m
        res = fib_mod(d, m)
        results.append(res)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()