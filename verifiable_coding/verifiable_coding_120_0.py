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
        m = int(data[index+1])
        index += 2
        
        if m == 0:
            results.append(0)
            continue
        
        # The maximum value of f(s) is achieved when the '1's are spread out as much as possible
        # So we place the '1's in such a way that they are separated by as many '0's as possible
        # The number of substrings that contain at least one '1' is equal to total substrings - substrings of all '0's
        # Total substrings is n*(n+1)//2
        total_substrings = n * (n + 1) // 2
        
        # Number of substrings of all '0's: if there are k groups of consecutive '0's, then the number of substrings is sum(i*(i+1)//2 for i in group_lengths)
        # To minimize this, we want to maximize the number of '1's, which is already done by spreading them out
        # So the maximum value of f(s) is total_substrings - (number of substrings of all '0's)
        
        # When '1's are spread out, the number of '0's between them is (m-1) groups of '0's, each of length (n - m) // m
        # But since we want to maximize the number of substrings with at least one '1', we should minimize the number of '0's between '1's
        # So the optimal arrangement is to have the '1's as spread out as possible, with as many '0's between them as possible
        
        # The number of substrings of all '0's is the sum of (length of each group of '0's) * (length + 1) // 2
        # The optimal arrangement is to have the '1's as spread out as possible, which means the '0's are grouped as evenly as possible
        
        # The number of '0's is n - m
        zeros = n - m
        
        # If there are m '1's, then there are m+1 groups of '0's (before the first '1', between '1's, and after the last '1')
        # So we distribute the zeros as evenly as possible among m+1 groups
        # Each group gets either (zeros // (m+1)) or (zeros // (m+1)) + 1 zeros
        # The number of groups with (zeros // (m+1)) + 1 zeros is (zeros % (m+1))
        
        group_size = zeros // (m + 1)
        extra_groups = zeros % (m + 1)
        
        # The number of substrings of all '0's is sum of (i*(i+1)//2 for i in group_lengths)
        # Each group has either group_size or group_size + 1 zeros
        # So the total is (m + 1 - extra_groups) * group_size * (group_size + 1) // 2 + extra_groups * (group_size + 1) * (group_size + 2) // 2
        
        total_zeros_substrings = (m + 1 - extra_groups) * group_size * (group_size + 1) // 2
        total_zeros_substrings += extra_groups * (group_size + 1) * (group_size + 2) // 2
        
        results.append(total_substrings - total_zeros_substrings)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()