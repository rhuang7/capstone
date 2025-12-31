import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    result = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        
        a_bits = bin(A)[2:]
        b_bits = bin(B)[2:]
        c_bits = bin(C)[2:]
        
        len_c = len(c_bits)
        len_a = len(a_bits)
        len_b = len(b_bits)
        
        # Pad with leading zeros to make all same length
        a_bits = a_bits.zfill(len_c)
        b_bits = b_bits.zfill(len_c)
        c_bits = c_bits.zfill(len_c)
        
        # Count the number of 1s in each bit position
        a_ones = [0] * len_c
        b_ones = [0] * len_c
        c_ones = [0] * len_c
        
        for i in range(len_c):
            a_ones[i] = int(a_bits[i])
            b_ones[i] = int(b_bits[i])
            c_ones[i] = int(c_bits[i])
        
        # Check if the sum of bits in each position matches C
        valid = True
        for i in range(len_c):
            if (a_ones[i] + b_ones[i]) != c_ones[i]:
                valid = False
                break
        
        if not valid:
            result.append(0)
            continue
        
        # Count the number of ways to permute the bits
        # For each bit position, count how many 1s are in A and B
        # The number of ways is the product of combinations of choosing positions for 1s in A and B
        
        # Count the number of 1s in A and B
        a_ones_count = sum(a_ones)
        b_ones_count = sum(b_ones)
        
        # The number of ways is the product of combinations of choosing a_ones_count positions for 1s in A and b_ones_count positions for 1s in B
        # But we need to ensure that the total number of 1s in A and B is equal to the number of 1s in C
        
        # The total number of 1s in C is sum(c_ones)
        c_ones_count = sum(c_ones)
        
        if a_ones_count + b_ones_count != c_ones_count:
            result.append(0)
            continue
        
        # Compute the number of ways
        from math import comb
        
        # The number of ways is comb(len_c, a_ones_count) * comb(len_c - a_ones_count, b_ones_count)
        ways = comb(len_c, a_ones_count) * comb(len_c - a_ones_count, b_ones_count)
        result.append(ways)
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == '__main__':
    solve()