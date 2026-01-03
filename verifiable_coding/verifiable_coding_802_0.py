import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    result = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        
        # Convert A, B, C to binary strings without leading '0b'
        a_bin = bin(A)[2:]
        b_bin = bin(B)[2:]
        c_bin = bin(C)[2:]
        
        # Count the number of 1s in each binary
        a_ones = a_bin.count('1')
        b_ones = b_bin.count('1')
        c_ones = c_bin.count('1')
        
        # If the number of 1s in A + B != C, it's impossible
        if a_ones + b_ones != c_ones:
            result.append(0)
            continue
        
        # Get the length of the longest binary string
        max_len = max(len(a_bin), len(b_bin), len(c_bin))
        
        # Pad the binary strings with leading zeros to make them the same length
        a_bin = a_bin.zfill(max_len)
        b_bin = b_bin.zfill(max_len)
        c_bin = c_bin.zfill(max_len)
        
        # Count the number of positions where a and b have 1s and c has 0s
        # This is the number of positions where a and b have 1s but c has 0s
        # This is not allowed because a + b = c
        invalid = 0
        for i in range(max_len):
            if a_bin[i] == '1' and b_bin[i] == '1' and c_bin[i] == '0':
                invalid += 1
        
        # If there are invalid positions, it's impossible
        if invalid > 0:
            result.append(0)
            continue
        
        # Count the number of positions where a has 1 and b has 0
        # These can be swapped with positions where a has 0 and b has 1
        # The number of such positions is the number of ways to swap
        swap_count = 0
        for i in range(max_len):
            if a_bin[i] == '1' and b_bin[i] == '0':
                swap_count += 1
        
        # The number of ways is (swap_count)! / (swap_count - swap_count)! = swap_count! / 0! = swap_count!
        # But since we can choose any subset of the swap positions to swap, the number of ways is 2^swap_count
        # Because for each swap position, we can choose to swap or not
        # However, we must ensure that the total number of 1s in a and b is the same as in c
        # Which we have already checked
        # So the answer is 2^swap_count
        result.append(2 ** swap_count)
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == '__main__':
    solve()