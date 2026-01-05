import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        max_remainder = 0
        best_A = 1
        for A in range(1, N+1):
            remainder = N % A
            if remainder > max_remainder:
                max_remainder = remainder
                best_A = A
            elif remainder == max_remainder:
                if A > best_A:
                    best_A = A
        print(best_A)

if __name__ == '__main__':
    solve()