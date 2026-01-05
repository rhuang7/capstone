import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N == 1:
            print(10)
        else:
            # The Nth smallest Aadhar number with sum of digits divisible by 10 and > 0
            # The sum of digits of N is s, then the required number is N + (10 - s % 10)
            s = sum(int(d) for d in str(N))
            add = (10 - s % 10) % 10
            result = N + add
            print(result)

if __name__ == '__main__':
    solve()