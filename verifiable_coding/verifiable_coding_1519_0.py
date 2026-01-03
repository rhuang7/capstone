import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Xs = list(map(int, data[1:T+1]))
    
    for X in Xs:
        if X == 2:
            print(2)
            continue
        # Find the smallest number >= X such that the XOR of the number with any other number < X is greater than the number
        # This is equivalent to finding the next number after X that is not a power of two
        # The smallest such number is X + 1 if X is a power of two, otherwise X
        if (X & (X - 1)) == 0:
            print(X + 1)
        else:
            print(X)

if __name__ == '__main__':
    solve()