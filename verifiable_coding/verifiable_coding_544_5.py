import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        
        result = ""
        for i in range(0, N, 4):
            bits = S[i:i+4]
            letter = decode_bits(bits)
            result += letter
        
        print(result)
    
def decode_bits(bits):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    current = 0
    for bit in bits:
        if bit == '1':
            current = 1 - current
        current = (current << 1) & 0b1111
    return letters[current]