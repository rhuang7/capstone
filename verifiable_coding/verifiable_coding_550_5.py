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
        bits_A = A.bit_length()
        bits_B = B.bit_length()
        
        # Pad with leading zeros to make the number of bits equal
        A_padded = A
        B_padded = B
        
        if bits_A < bits_B:
            A_padded = A << (bits_B - bits_A)
        elif bits_B < bits_A:
            B_padded = B << (bits_A - bits_B)
        
        # Function to perform right circular shift on B
        def right_circular_shift(b, bits):
            return ((b >> 1) & ( (1 << bits) - 1 )) | ( (b & 1) << (bits - 1) )
        
        max_xor = 0
        best_shifts = 0
        
        # Try all possible shifts (up to bits_B)
        for shifts in range(bits_B):
            # Perform shift
            B_shifted = right_circular_shift(B_padded, bits_B)
            
            # Compute XOR
            current_xor = A_padded ^ B_shifted
            
            # Update max_xor and best_shifts
            if current_xor > max_xor:
                max_xor = current_xor
                best_shifts = shifts
        
        results.append(f"{best_shifts} {max_xor}")
    
    print("\n".join(results))