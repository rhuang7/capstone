import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        
        # Find the number of bits for A and B
        bits_A = A.bit_length()
        bits_B = B.bit_length()
        
        # Make sure both have the same number of bits by padding with leading zeros
        # For A, pad with leading zeros to match the number of bits of B
        # For B, pad with leading zeros to match the number of bits of A
        # But since we need to make them have the same number of bits, we can just use the max of the two
        max_bits = max(bits_A, bits_B)
        
        # Convert A and B to binary strings with leading zeros to have max_bits length
        A_bin = bin(A)[2:].zfill(max_bits)
        B_bin = bin(B)[2:].zfill(max_bits)
        
        # Convert B_bin to integer
        B_val = int(B_bin, 2)
        
        # Generate all possible right circular shifts of B
        # For each shift, compute A ^ B and track the maximum
        max_xor = 0
        best_shift = 0
        
        for shift in range(max_bits):
            # Perform right circular shift
            B_shift = B_bin[-1] + B_bin[:-1]
            current_B = int(B_shift, 2)
            current_xor = A ^ current_B
            
            if current_xor > max_xor:
                max_xor = current_xor
                best_shift = shift
        
        results.append(f"{best_shift} {max_xor}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()