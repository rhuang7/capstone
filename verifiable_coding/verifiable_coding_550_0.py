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
        bits_A = A.bit_length()
        bits_B = B.bit_length()
        
        # Pad with leading zeros to make the number of bits equal
        A_padded = A
        B_padded = B
        
        if bits_A < bits_B:
            A_padded = A << (bits_B - bits_A)
        elif bits_B < bits_A:
            B_padded = B << (bits_A - bits_B)
        
        # Get the binary representation of B_padded
        bin_B = bin(B_padded)[2:]
        length = len(bin_B)
        
        # Generate all possible right circular shifts of B_padded
        max_xor = 0
        best_shift = 0
        
        for shift in range(length):
            # Perform right circular shift
            shifted_B = (B_padded >> 1) | (B_padded << (length - 1)) & ((1 << length) - 1)
            B_padded = shifted_B
            
            # Compute XOR with A_padded
            current_xor = A_padded ^ B_padded
            
            if current_xor > max_xor:
                max_xor = current_xor
                best_shift = shift
        
        results.append(f"{best_shift} {max_xor}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()