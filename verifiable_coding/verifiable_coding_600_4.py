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
        # So the final position is 2^(k) where k is the number of times we can divide (N-1) by 2
        # We need to find the position in the original sequence that survives all the steps
        # The position is 2^(floor(log2(N-1))) 
        # So we find the highest power of 2 less than or equal to N-1
        # Then find the Fibonacci number at that position modulo 10
        # We can precompute the Fibonacci numbers modulo 10 up to 60 (since the Pisano period for 10 is 60)
        fib_mod_10 = [0, 1]
        for i in range(2, 60):
            fib_mod_10.append((fib_mod_10[i-1] + fib_mod_10[i-2]) % 10)
        # Find the highest power of 2 less than or equal to N-1
        power = 1
        while power * 2 <= N - 1:
            power *= 2
        print(fib_mod_10[power - 1])

if __name__ == '__main__':
    solve()