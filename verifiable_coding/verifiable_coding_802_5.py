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
        
        # Convert to binary strings, including leading zeros to match the length of C's binary
        bin_A = bin(A)[2:]
        bin_B = bin(B)[2:]
        bin_C = bin(C)[2:]
        
        # Find the maximum length of the binary strings
        max_len = max(len(bin_A), len(bin_B), len(bin_C))
        
        # Pad with leading zeros to make all binary strings the same length
        bin_A = bin_A.zfill(max_len)
        bin_B = bin_B.zfill(max_len)
        bin_C = bin_C.zfill(max_len)
        
        # Count the number of 1s in each binary string
        count_A = bin_A.count('1')
        count_B = bin_B.count('1')
        count_C = bin_C.count('1')
        
        # Check if the number of 1s in A and B is equal to the number of 1s in C
        if count_A + count_B != count_C:
            result.append(0)
            continue
        
        # Calculate the number of ways to permute the bits of A and B such that their sum is C
        # The number of ways is (number of permutations of A's bits) * (number of permutations of B's bits)
        # But we must ensure that the sum of the permuted bits equals C
        
        # We can use dynamic programming to count the number of valid permutations
        # However, for the sake of efficiency and given the constraints, we can use a bitmask approach
        
        # Since the maximum number of bits is 30 (since 2^30 is about 1e9), we can use a bitmask approach
        # We'll generate all possible permutations of A's bits and B's bits and check if their sum is C
        
        # Generate all possible permutations of A's bits
        from itertools import permutations
        
        # Generate all possible permutations of A's bits
        a_bits = list(bin_A)
        a_perms = set(permutations(a_bits))
        
        # Generate all possible permutations of B's bits
        b_bits = list(bin_B)
        b_perms = set(permutations(b_bits))
        
        # Count the number of valid pairs (a_perm, b_perm) such that their sum is C
        count = 0
        for a_perm in a_perms:
            a_val = int(''.join(a_perm), 2)
            for b_perm in b_perms:
                b_val = int(''.join(b_perm), 2)
                if a_val + b_val == C:
                    count += 1
        
        result.append(count)
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == '__main__':
    solve()