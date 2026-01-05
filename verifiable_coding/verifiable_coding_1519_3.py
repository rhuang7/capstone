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
        # So we find the next number after X that has a higher bit set than X
        # For example, for X = 3 (binary 11), the next number is 4 (100)
        # For X = 7 (111), the next number is 8 (1000)
        # So we find the next power of two greater than X
        # The next power of two after X is 2^(floor(log2(X)) + 1)
        # So we compute the next power of two after X
        # If X is a power of two, then the next power of two is X * 2
        # Otherwise, it's 2^(floor(log2(X)) + 1)
        # So we can compute it as (X & -X) << 1 if X is not a power of two, else X << 1
        # But we can also compute it as the next power of two after X
        # So we can compute it as 1 << (X.bit_length())
        res = 1 << (X.bit_length())
        print(res)
        
if __name__ == '__main__':
    solve()