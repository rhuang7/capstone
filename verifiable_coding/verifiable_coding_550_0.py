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
        
        # Find the number of bits in A and B
        len_A = A.bit_length()
        len_B = B.bit_length()
        
        # Pad with leading zeros to make the lengths equal
        A_padded = A
        B_padded = B
        
        # If lengths are different, pad the shorter one with leading zeros
        if len_A < len_B:
            A_padded = A << (len_B - len_A)
        elif len_B < len_A:
            B_padded = B << (len_A - len_B)
        
        # Now A_padded and B_padded have the same number of bits
        
        # Generate all possible right circular shifts of B_padded
        # and compute A^B for each shift
        max_xor = 0
        best_shift = 0
        
        # Get the binary representation of B_padded
        bin_B = bin(B_padded)[2:]
        len_B = len(bin_B)
        
        # Generate all possible shifts
        for shift in range(len_B):
            # Right circular shift by shift positions
            shifted_B = (B_padded >> shift) | (B_padded << (len_B - shift)) & ((1 << len_B) - 1)
            xor = A_padded ^ shifted_B
            if xor > max_xor:
                max_xor = xor
                best_shift = shift
        
        results.append(f"{best_shift} {max_xor}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()