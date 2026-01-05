import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        N = int(data[index+2])
        index += 3
        
        if X == Y:
            results.append(0)
            continue
        
        # Determine the first bit where X and Y differ
        diff = X ^ Y
        pos = 0
        while diff:
            if diff & 1:
                break
            diff >>= 1
            pos += 1
        
        # Count the number of Z such that (X ^ Z) < (Y ^ Z)
        # This happens when the first differing bit between X and Y is set in Z
        # So, for Z in [0, N], count how many have that bit set
        count = 0
        mask = 1 << pos
        for z in range(N + 1):
            if (z & mask) != 0:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()