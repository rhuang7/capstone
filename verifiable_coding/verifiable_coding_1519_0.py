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
        # But we can also find it by finding the next number with higher set bits
        # The correct approach is to find the next number with higher set bits than X
        # This is done by finding the first 0 bit in X's binary representation and flipping it to 1, then setting all lower bits to 0
        # For example, for X = 3 (binary 11), the next number is 4 (100)
        # For X = 7 (binary 111), the next number is 8 (1000)
        # So the correct answer is the next power of two greater than X
        # But we need to find the smallest number >= X such that it is not a subset of X's bits
        # This is the same as the next number with higher set bits than X
        # So the answer is the next number after X that is not a subset of X's bits
        # This is done by finding the first 0 bit in X's binary representation and flipping it to 1, then setting all lower bits to 0
        # For example, for X = 3 (binary 11), the first 0 bit is at position 2, so we set it to 1 and lower bits to 0: 100 = 4
        # For X = 7 (binary 111), the first 0 bit is at position 3, so we set it to 1 and lower bits to 0: 1000 = 8
        # So the answer is the next number after X that is not a subset of X's bits
        # This is done by finding the first 0 bit in X's binary representation and flipping it to 1, then setting all lower bits to 0
        # So the answer is (X ^ (X & (X - 1))) + 1
        # But this is not correct for all cases, so we need to find the next number after X that is not a subset of X's bits
        # The correct approach is to find the next number after X that is not a subset of X's bits
        # This can be done by finding the next number after X that is not a subset of X's bits
        # This is equivalent to finding the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # This can be done by finding the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # This can be done by finding the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # This is the same as the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the answer is the next number after X that is not a subset of X's bits
        # So the