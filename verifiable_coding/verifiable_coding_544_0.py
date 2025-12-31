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
            letter = 0
            for bit in bits:
                letter = (letter << 1) | int(bit)
            result += chr(ord('a') + letter)
        
        print(result)
        
if __name__ == '__main__':
    solve()