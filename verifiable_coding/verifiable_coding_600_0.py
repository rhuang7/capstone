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
        # The process is equivalent to finding the (2^k)-th element in the sequence
        # where k is the number of times you can divide (N-1) by 2
        # So we find the highest power of 2 less than or equal to N-1
        k = 0
        while (1 << (k + 1)) <= N - 1:
            k += 1
        pos = 1 << k
        # Compute Fibonacci numbers modulo 10 up to pos
        a, b = 0, 1
        for _ in range(pos - 1):
            a, b = b, (a + b) % 10
        print(b)

if __name__ == '__main__':
    solve()