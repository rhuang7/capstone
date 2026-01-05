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
        msb = 0
        while diff:
            diff >>= 1
            msb += 1
        
        # The number of Z where (X ^ Z) < (Y ^ Z) is determined by the most significant bit where X and Y differ
        # If the most significant bit where X and Y differ is set in X, then half of the Z values will satisfy the condition
        # If it is set in Y, then half will not satisfy the condition
        # The remaining bits can be anything
        count = (1 << msb) // 2
        
        # If N is less than the most significant bit position, then all Z values are valid
        if N < (1 << msb):
            results.append(N + 1)
        else:
            results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()