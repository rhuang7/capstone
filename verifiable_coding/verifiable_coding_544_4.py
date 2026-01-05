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
        
        result = []
        for i in range(0, N, 4):
            bits = S[i:i+4]
            letter = 'a'
            low = 0
            high = 15
            for bit in bits:
                if bit == '0':
                    high = (low + high) // 2
                else:
                    low = (low + high) // 2 + 1
            result.append(chr(ord('a') + low))
        print(''.join(result))
        
if __name__ == '__main__':
    solve()