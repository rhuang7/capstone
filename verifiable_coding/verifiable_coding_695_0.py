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
        
        # If X == Y, then (X ^ Z) == (Y ^ Z) for all Z, so answer is 0
        if X == Y:
            results.append(0)
            continue
        
        # Compute the difference between Y and X
        diff = Y ^ X
        # Find the most significant bit (MSB) where Y and X differ
        msb = 0
        while diff >> msb == 0:
            msb += 1
        
        # For Z in [0, N], count how many have (X ^ Z) < (Y ^ Z)
        # This is equivalent to counting how many Z have the MSB where X and Y differ set to 0 in (X ^ Z)
        count = 0
        for z in range(0, N + 1):
            if (X ^ z) < (Y ^ z):
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()