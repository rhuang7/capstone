import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        if m == 0:
            results.append(0)
            continue
        
        # The maximum f(s) is achieved when 1's are as spread out as possible
        # So we place 1's in such a way that they are separated by as many 0's as possible
        # The number of substrings that contain at least one '1' is total substrings - substrings of all 0's
        
        total_substrings = n * (n + 1) // 2
        zero_blocks = n - m
        
        # The maximum number of substrings of all 0's is the sum of (length of each block of 0's) * (length + 1) // 2
        # To minimize this, we want to spread the 0's as evenly as possible among the m 1's
        # So we have m + 1 blocks of 0's (before, between, and after the 1's)
        # The number of 0's in each block is either zero or one
        # So the maximum number of substrings of all 0's is the sum of (k * (k + 1)) // 2 for k in the zero blocks
        
        # The number of zero blocks is m + 1
        # The number of 0's in each block is (zero_blocks) // (m + 1) or (zero_blocks) // (m + 1) + 1
        # So we have (zero_blocks % (m + 1)) blocks with (zero_blocks // (m + 1) + 1) 0's
        # and (m + 1 - zero_blocks % (m + 1)) blocks with (zero_blocks // (m + 1)) 0's
        
        k = zero_blocks // (m + 1)
        rem = zero_blocks % (m + 1)
        
        sum_zero = 0
        for i in range(rem):
            sum_zero += (k + 1) * (k + 2) // 2
        for i in range(m + 1 - rem):
            sum_zero += k * (k + 1) // 2
        
        results.append(total_substrings - sum_zero)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()