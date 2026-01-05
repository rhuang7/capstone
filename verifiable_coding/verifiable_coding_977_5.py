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
        
        # Step 1: Swap characters in pairs
        swapped = list(S)
        for i in range(0, N - 1, 2):
            if i + 1 < N:
                swapped[i], swapped[i+1] = swapped[i+1], swapped[i]
        
        # Step 2: Replace each character with its opposite in the alphabet
        encoded = []
        for c in swapped:
            if 'a' <= c <= 'z':
                encoded.append(chr(ord('a') + ord('z') - ord(c)))
        
        print(''.join(encoded))
        
if __name__ == '__main__':
    solve()