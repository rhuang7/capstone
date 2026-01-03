import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        # The number of ways to reach N stairs is equal to the (N+1)th Fibonacci number
        # because the problem is equivalent to counting the number of ways to climb N stairs
        # with steps of 1 or 2, where order does not matter.
        # This is the same as the Fibonacci sequence starting from 1, 1, 2, 3, 5, ...
        a, b = 1, 1
        for _ in range(N):
            a, b = b, a + b
        results.append(b)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()