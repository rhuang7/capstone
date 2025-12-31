import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        # The number of ways to reach N stairs is the (N+1)th Fibonacci number
        # Since the chef can take 1 or 2 steps at a time
        a, b = 1, 1
        for _ in range(N):
            a, b = b, a + b
        results.append(b)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()