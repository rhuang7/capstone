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
        bin_A = bin(A)[2:]
        bin_B = bin(B)[2:]
        bin_C = bin(C)[2:]
        
        # Pad with leading zeros to make lengths equal
        max_len = max(len(bin_A), len(bin_B), len(bin_C))
        bin_A = bin_A.zfill(max_len)
        bin_B = bin_B.zfill(max_len)
        bin_C = bin_C.zfill(max_len)
        
        # Count the number of 1s in each binary string
        cnt_A = bin_A.count('1')
        cnt_B = bin_B.count('1')
        cnt_C = bin_C.count('1')
        
        # Check if the number of 1s in A and B is equal to that in C
        if cnt_A + cnt_B != cnt_C:
            results.append(0)
            continue
        
        # Count the number of positions where A and B have 1s
        # and where C has 1s
        # We need to find the number of ways to assign the 1s in A and B to the 1s in C
        # such that each 1 in C is covered by exactly one 1 from A or B
        
        # Count the number of positions where A has 1 and B has 0
        a1_b0 = 0
        # Count the number of positions where A has 0 and B has 1
        a0_b1 = 0
        # Count the number of positions where A and B both have 1
        a1_b1 = 0
        # Count the number of positions where A and B both have 0
        a0_b0 = 0
        
        for a, b, c in zip(bin_A, bin_B, bin_C):
            if a == '1' and b == '0' and c == '1':
                a1_b0 += 1
            elif a == '0' and b == '1' and c == '1':
                a0_b1 += 1
            elif a == '1' and b == '1' and c == '1':
                a1_b1 += 1
            elif a == '0' and b == '0' and c == '0':
                a0_b0 += 1
        
        # The number of ways is the product of combinations
        # For a1_b0: choose which of the a1_b0 positions are assigned to A
        # For a0_b1: choose which of the a0_b1 positions are assigned to B
        # For a1_b1: choose which of the a1_b1 positions are assigned to A
        # The rest are assigned to B
        
        from math import comb
        
        ways = 1
        ways *= comb(a1_b0, a1_b0)  # All go to A
        ways *= comb(a0_b1, a0_b1)  # All go to B
        ways *= comb(a1_b1, a1_b1)  # All go to A
        ways *= comb(a0_b0, a0_b0)  # All go to B
        
        results.append(ways)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()