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
        
        # Make sure both have the same number of bits by padding with leading zeros
        # We need to pad the smaller one with leading zeros to match the larger one
        if bits_A < bits_B:
            A = A << (bits_B - bits_A)
        elif bits_B < bits_A:
            B = B << (bits_A - bits_B)
        
        # Now A and B have the same number of bits
        # Generate all possible right circular shifts of B
        # The number of shifts is equal to the number of bits
        max_xor = 0
        best_shift = 0
        
        for shift in range(bits_A):
            # Perform right circular shift of B
            # Extract the last bit and move it to the front
            last_bit = (B >> (bits_A - 1)) & 1
            B = (B << 1) & ((1 << bits_A) - 1)
            B = (B | (last_bit << (bits_A - 1)))
            
            # Compute XOR
            current_xor = A ^ B
            if current_xor > max_xor:
                max_xor = current_xor
                best_shift = shift
        
        results.append(f"{best_shift} {max_xor}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()