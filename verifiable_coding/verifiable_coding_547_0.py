import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        pairs = []
        for _ in range(N):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            pairs.append((a, b))
        
        # Compute Grundy numbers for each pair
        grundy = []
        for a, b in pairs:
            # Compute the Grundy number for the pair (a, b)
            # This is equivalent to the game of Nimbers for the Euclidean algorithm
            # The Grundy number is the number of times you can subtract the smaller from the larger
            # until they are equal
            x, y = a, b
            if x > y:
                x, y = y, x
            g = 0
            while y != x:
                if x > y:
                    x, y = y, x
                g += 1
                y %= x
            grundy.append(g)
        
        # XOR all Grundy numbers
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        
        if xor_sum != 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()