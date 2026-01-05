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
        
        # Find the first bit where X and Y differ
        diff = X ^ Y
        first_diff_bit = diff.bit_length() - 1
        
        # For Z in [0, N], count how many have (X ^ Z) < (Y ^ Z)
        # This depends on the first differing bit between X and Y
        # If X has 0 at the first differing bit and Y has 1, then (X ^ Z) < (Y ^ Z)
        # If X has 1 and Y has 0, then (X ^ Z) > (Y ^ Z)
        # So we need to count how many Z in [0, N] have the first differing bit as 0 in X and 1 in Y
        
        # The first differing bit is known
        # We need to count how many Z in [0, N] have that bit as 0 in X and 1 in Y
        # Which is equivalent to Z having that bit as 1
        
        # So we count how many numbers in [0, N] have the first_diff_bit set to 1
        # This is equal to (N + 1) - (1 << first_diff_bit) if (1 << first_diff_bit) <= N + 1
        # Otherwise, it's 0
        
        count = 0
        mask = 1 << first_diff_bit
        if mask <= N + 1:
            count = (N + 1) - mask
        else:
            count = 0
        
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()