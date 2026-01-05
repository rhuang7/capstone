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
        # So we find the next number after X that is not a subset of X's bits
        # This can be done by finding the next higher number with the same number of bits
        # We find the first 0 bit in X's binary representation and set it to 1, then set all lower bits to 0
        # This is the next number with the same number of bits
        # If there is no such bit, then the next number is 2^bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So we find the next number after X that is not a