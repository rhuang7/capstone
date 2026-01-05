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
        
        # The maximum value of f(s) is achieved when the '1's are spread out as much as possible
        # So, the '1's are placed in such a way that they are separated by as many '0's as possible
        # The formula for maximum f(s) is:
        # total_substrings = n * (n + 1) // 2 - (number of substrings with no '1's)
        # The number of substrings with no '1's is the sum of (length of consecutive '0's) * (length of consecutive '0's + 1) // 2
        # To maximize f(s), we need to minimize the number of such substrings, which happens when the '1's are spread out as much as possible
        
        # The optimal arrangement is to place the '1's in positions that separate the string into m + 1 blocks of '0's
        # The number of '0's in each block is as equal as possible
        # Let's calculate the number of substrings with no '1's
        
        # Total number of substrings in the string is n*(n+1)//2
        total_substrings = n * (n + 1) // 2
        
        # The number of '0's is n - m
        # These '0's are divided into m + 1 blocks
        # Each block has either (n - m) // (m + 1) or (n - m) // (m + 1) + 1 '0's
        zeros = n - m
        block_size = zeros // (m + 1)
        remainder = zeros % (m + 1)
        
        # Calculate the sum of (length of block) * (length of block + 1) // 2 for all blocks
        sum_zeros_substrings = 0
        for i in range(remainder):
            sum_zeros_substrings += (block_size + 1) * (block_size + 2) // 2
        for i in range(m + 1 - remainder):
            sum_zeros_substrings += block_size * (block_size + 1) // 2
        
        max_f = total_substrings - sum_zeros_substrings
        results.append(max_f)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()