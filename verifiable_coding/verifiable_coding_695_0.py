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
        # Find the most significant bit where Y and X differ
        msb = diff.bit_length() - 1
        
        # Count the number of Z where (X ^ Z) < (Y ^ Z)
        # This is equivalent to finding Z where the most significant differing bit between X and Y is set in Z
        # So we count the number of Z where the msb is set in Z
        count = 0
        for z in range(N + 1):
            if (z >> msb) & 1:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()