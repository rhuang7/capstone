import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        N = int(data[index+2])
        index += 3
        
        if X == Y:
            results.append(0)
            continue
        
        # Compute the first differing bit
        diff = X ^ Y
        first_diff_bit = diff.bit_length() - 1
        
        # Count the number of Z where (X ^ Z) < (Y ^ Z)
        # This happens when the first differing bit in (X ^ Z) and (Y ^ Z) is set in X ^ Z but not in Y ^ Z
        # So, for Z, the bit at first_diff_bit must be 0 if X has 1 and Y has 0, or 1 if X has 0 and Y has 1
        
        # Determine which bit is set in X and Y
        x_bit = (X >> first_diff_bit) & 1
        y_bit = (Y >> first_diff_bit) & 1
        
        # If X has 1 and Y has 0, then Z's bit must be 0
        # If X has 0 and Y has 1, then Z's bit must be 1
        # Otherwise, the rest of the bits don't matter
        if x_bit == 1 and y_bit == 0:
            # Z's bit must be 0
            count = 1 << first_diff_bit
            if N >= (1 << first_diff_bit):
                count = (1 << first_diff_bit)
            else:
                count = N + 1
            results.append(count)
        elif x_bit == 0 and y_bit == 1:
            # Z's bit must be 1
            count = (1 << first_diff_bit) - 1
            if N >= (1 << first_diff_bit) - 1:
                count = (1 << first_diff_bit) - 1
            else:
                count = N + 1
            results.append(count)
        else:
            # The first differing bit is not set in both, so the rest of the bits determine the comparison
            # The number of Z is N + 1
            results.append(N + 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()