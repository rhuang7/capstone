import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        # The number of ways to reach N stairs with steps of 1 or 2 is the (N+1)th Fibonacci number
        # Since order doesn't matter, it's the number of partitions of N into 1s and 2s
        # This is equivalent to the (N+1)th Fibonacci number
        a, b = 1, 1
        for _ in range(N):
            a, b = b, a + b
        results.append(b)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()