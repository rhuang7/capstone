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
        index += 2
        
        # Find the number of bits in A and B
        a_bits = A.bit_length()
        b_bits = B.bit_length()
        
        # Ensure both have the same number of bits by padding with leading zeros
        # For A, pad with (b_bits - a_bits) leading zeros
        # For B, pad with (a_bits - b_bits) leading zeros
        a_padded = A
        b_padded = B
        
        if a_bits < b_bits:
            a_padded = A << (b_bits - a_bits)
        elif b_bits < a_bits:
            b_padded = B << (a_bits - b_bits)
        
        # Function to perform right circular shift on B
        def right_circular_shift(b, bits):
            # Get the bit representation
            bits_str = bin(b)[2:].zfill(bits)
            # Perform right circular shift
            shifted = bits_str[-1] + bits_str[:-1]
            # Convert back to integer
            return int(shifted, 2)
        
        max_xor = 0
        best_shifts = 0
        
        # Try all possible shifts (up to bits-1)
        for shifts in range(bits):
            # Apply shifts to B
            current_b = right_circular_shift(b_padded, bits)
            current_xor = a_padded ^ current_b
            if current_xor > max_xor:
                max_xor = current_xor
                best_shifts = shifts
        
        results.append(f"{best_shifts} {max_xor}")
    
    print("\n".join(results))