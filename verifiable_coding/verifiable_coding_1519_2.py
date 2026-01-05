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
        # This is equivalent to finding the smallest number >= X that is not a subset of X's bits
        # The smallest such number is X | (X >> 1) | (X >> 2) | ... until the highest bit
        # We can compute it as X + (X & -X)
        # But for correctness, we can find the next number with higher value than X and not a subset of X's bits
        # The correct answer is X + (X & -X)
        res = X + (X & -X)
        print(res)

if __name__ == '__main__':
    solve()