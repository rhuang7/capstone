import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        
        # Convert to binary strings
        a_bin = bin(A)[2:]
        b_bin = bin(B)[2:]
        c_bin = bin(C)[2:]
        
        # Count the number of 1s in each binary
        a_ones = a_bin.count('1')
        b_ones = b_bin.count('1')
        c_ones = c_bin.count('1')
        
        # Check if the number of 1s in A and B combined is equal to the number of 1s in C
        if a_ones + b_ones != c_ones:
            results.append(0)
            continue
        
        # Count the number of 1s in C that are not in A or B
        c_ones_not_in_ab = c_ones - a_ones - b_ones
        
        # The number of ways is the product of the combinations of bits in A and B
        # For each bit in A, it can be in any position, and same for B
        # But we need to ensure that the total number of 1s in C is correct
        # The number of ways is (number of ways to arrange A's bits) * (number of ways to arrange B's bits)
        # But we have to consider that some bits in C are not in A or B
        
        # The number of ways to arrange A's bits is (number of bits in A)! / (number of 0s! * number of 1s!)
        # Similarly for B
        
        # Calculate the number of bits in A and B
        len_a = len(a_bin)
        len_b = len(b_bin)
        
        # Calculate the number of 0s in A and B
        a_zeros = len_a - a_ones
        b_zeros = len_b - b_ones
        
        # Calculate the number of ways to arrange A's bits
        from math import comb
        
        ways_a = comb(len_a, a_ones)
        ways_b = comb(len_b, b_ones)
        
        # The number of ways to arrange the bits of C that are not in A or B
        # These bits must be in the same positions as the bits of A and B
        # So we need to calculate the number of ways to arrange these bits
        
        # The number of positions where C has 1s not in A or B is c_ones_not_in_ab
        # The number of positions where C has 0s not in A or B is (len_a + len_b - c_ones_not_in_ab)
        
        # The number of ways to arrange these bits is comb(len_a + len_b, c_ones_not_in_ab)
        total_positions = len_a + len_b
        ways_c = comb(total_positions, c_ones_not_in_ab)
        
        # The total number of ways is the product of the ways to arrange A, B, and C
        total_ways = ways_a * ways_b * ways_c
        
        results.append(total_ways)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()