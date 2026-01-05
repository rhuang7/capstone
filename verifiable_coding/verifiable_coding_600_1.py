import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    for N in N_list:
        if N == 1:
            print(0)
            continue
        if N == 2:
            print(1)
            continue
        # Find the position of the last remaining element
        # The process reduces the length of the sequence by half each time
        # So the final element is at position 2^(k) where k is the number of times we can divide (N-1) by 2
        # We need to find the position in the original sequence
        # The position is 2^m where m is the number of times we can divide (N-1) by 2
        # So we compute the highest power of 2 less than or equal to N-1
        # Then find the Fibonacci number at that position modulo 10
        m = 0
        while (1 << (m + 1)) <= N - 1:
            m += 1
        pos = 1 << m
        # Compute Fibonacci numbers modulo 10
        a, b = 0, 1
        for _ in range(pos - 1):
            a, b = b, (a + b) % 10
        print(b)

if __name__ == '__main__':
    solve()