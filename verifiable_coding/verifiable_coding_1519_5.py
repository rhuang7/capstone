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
        # The smallest such number is X ^ (X & (X - 1)) + 1
        # Or, more simply, find the next number with a higher bit set
        # The next number after X that is not a subset of X's bits is X ^ (X & (X - 1)) + 1
        # But we can also find it by finding the next higher number with a higher bit set
        # For example, for X = 3 (binary 11), the next number is 4 (100)
        # For X = 7 (binary 111), the next number is 8 (1000)
        # So we can find the next number by finding the first 0 bit in X's binary representation and setting it to 1, then setting all lower bits to 0
        # This is equivalent to finding the next higher number with a higher bit set
        # So the answer is X ^ (X & (X - 1)) + 1
        # But we can also find it by finding the next number with a higher bit set
        # So the answer is (X & -X) << 1
        # But we need to make sure it's >= X
        # So the answer is (X & -X) << 1 if (X & -X) << 1 >= X else (X | (X + 1))
        # But for the given examples, the answer is simply the next power of two greater than or equal to X
        # So the answer is 1 << (X.bit_length())
        print(1 << (X.bit_length()))

if __name__ == '__main__':
    solve()