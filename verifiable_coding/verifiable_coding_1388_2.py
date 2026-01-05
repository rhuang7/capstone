import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:]))
    
    for N in N_list:
        if N <= 250000:
            print(N)
        elif N <= 500000:
            tax = (N - 250000) * 5 // 100
            print(N - tax)
        elif N <= 750000:
            tax = 250000 * 5 // 100 + (N - 500000) * 10 // 100
            print(N - tax)
        elif N <= 1000000:
            tax = 250000 * 5 // 100 + 250000 * 10 // 100 + (N - 750000) * 15 // 100
            print(N - tax)
        elif N <= 1250000:
            tax = 250000 * 5 // 100 + 250000 * 10 // 100 + 250000 * 15 // 100 + (N - 1000000) * 20 // 100
            print(N - tax)
        elif N <= 1500000:
            tax = 250000 * 5 // 100 + 250000 * 10 // 100 + 250000 * 15 // 100 + 250000 * 20 // 100 + (N - 1250000) * 25 // 100
            print(N - tax)
        else:
            tax = 250000 * 5 // 100 + 250000 * 10 // 100 + 250000 * 15 // 100 + 250000 * 20 // 100 + 250000 * 25 // 100 + (N - 1500000) * 30 // 100
            print(N - tax)

if __name__ == '__main__':
    solve()