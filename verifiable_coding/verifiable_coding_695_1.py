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
        
        # Count the number of Z such that (X ^ Z) < (Y ^ Z)
        # This is equivalent to finding the number of Z where the most significant bit where X and Y differ is set in Z
        # If the most significant bit is set in Z, then (Y ^ Z) > (X ^ Z)
        # If it is not set, then (Y ^ Z) < (X ^ Z)
        # So we need to count the number of Z where the most significant bit is not set
        # Which is (N + 1) // 2 if the bit is in the range of N
        # But we need to handle cases where the bit is higher than N
        count = 0
        if (1 << msb) <= N + 1:
            count = (N + 1) // 2
        else:
            count = N + 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()