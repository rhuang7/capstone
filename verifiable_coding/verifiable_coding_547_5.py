import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        pairs = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            idx += 2
            pairs.append((a, b))
        
        # Calculate Grundy numbers for each pair
        grundy = []
        for a, b in pairs:
            # Compute the Grundy number for the pair (a, b)
            # This is equivalent to the number of times you can subtract the smaller from the larger until they are equal
            # This is the same as the number of steps in the Euclidean algorithm
            x, y = a, b
            g = 0
            while x != y:
                if x > y:
                    x, y = y, x
                g += 1
                y %= x
            grundy.append(g)
        
        # The XOR of all Grundy numbers determines the winner
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        
        if xor_sum != 0:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()