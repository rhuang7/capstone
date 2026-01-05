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
        count_A = bin_A.count('1')
        count_B = bin_B.count('1')
        count_C = bin_C.count('1')
        
        # If the number of 1s in C is not equal to the sum of 1s in A and B, it's impossible
        if count_C != count_A + count_B:
            results.append(0)
            continue
        
        # Count the number of ways to arrange the bits of A and B such that their sum is C
        # We need to find the number of ways to choose positions for 1s in A and B such that their sum matches C
        # This is a combinatorial problem where we choose positions for 1s in A and B such that their sum matches C
        
        # Precompute the number of ways to choose positions for 1s in A and B
        # We need to find the number of ways to choose positions for 1s in A and B such that the sum of bits in each position is equal to the corresponding bit in C
        
        # We will use dynamic programming to count the number of valid ways
        # We will process each bit position from left to right
        # dp[i][j] = number of ways to assign bits to the first i positions such that A has j 1s so far
        
        # Initialize dp
        dp = [[0] * (count_A + 1) for _ in range(max_len + 1)]
        dp[0][0] = 1
        
        for i in range(1, max_len + 1):
            # Current bit of C
            c_bit = bin_C[i-1]
            # Current bit of A
            a_bit = bin_A[i-1]
            # Current bit of B
            b_bit = bin_B[i-1]
            
            # If the current bit of C is 1, then either A or B must have a 1 in this position
            if c_bit == '1':
                # A has 1, B has 0
                if a_bit == '1' and b_bit == '0':
                    for j in range(count_A + 1):
                        if j >= 1:
                            dp[i][j] += dp[i-1][j-1]
                # A has 0, B has 1
                if a_bit == '0' and b_bit == '1':
                    for j in range(count_A + 1):
                        if j >= 0:
                            dp[i][j] += dp[i-1][j]
                # A and B both have 1
                if a_bit == '1' and b_bit == '1':
                    for j in range(count_A + 1):
                        if j >= 1:
                            dp[i][j] += dp[i-1][j-1]
            else:
                # Current bit of C is 0, so both A and B must have 0 in this position
                if a_bit == '0' and b_bit == '0':
                    for j in range(count_A + 1):
                        dp[i][j] += dp[i-1][j]
                # If either A or B has 1, it's invalid
                else:
                    pass
        
        results.append(dp[max_len][count_A])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()