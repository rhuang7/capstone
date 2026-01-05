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
        
        # Find the number of bits for A and B
        len_A = A.bit_length()
        len_B = B.bit_length()
        
        # Pad with leading zeros to make the lengths equal
        A_padded = A
        B_padded = B
        
        # If lengths are not equal, pad B with leading zeros
        if len_A != len_B:
            diff = len_A - len_B
            B_padded = B << (diff)
        
        # Convert to binary strings
        bin_A = bin(A_padded)[2:]
        bin_B = bin(B_padded)[2:]
        
        # Generate all possible right circular shifts of B
        max_shift = len(bin_B)
        max_xor = 0
        best_shift = 0
        
        for shift in range(max_shift):
            # Perform right circular shift
            shifted_B = (B_padded >> shift) | (B_padded << (max_shift - shift)) & ((1 << max_shift) - 1)
            
            # Compute XOR
            xor = A_padded ^ shifted_B
            
            # Update max_xor and best_shift
            if xor > max_xor:
                max_xor = xor
                best_shift = shift
        
        results.append(f"{best_shift} {max_xor}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()