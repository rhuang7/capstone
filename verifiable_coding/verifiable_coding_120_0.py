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
        # So we place the 1's in such a way that they are separated by as many 0's as possible
        # The number of substrings with at least one 1 is total substrings - substrings of all 0's
        # Total substrings is n*(n+1)//2
        total_substrings = n * (n + 1) // 2
        
        # Substrings of all 0's: these are the parts between the 1's
        # If there are m 1's, there are m+1 groups of 0's
        # The maximum number of 0's between 1's is (n - m) // m, but we need to distribute them to maximize the number of 0's groups
        # So the number of 0's in each group is (n - m) // m, and some groups have one more 0
        # The number of substrings of all 0's is sum of (length of each group) * (length + 1) // 2
        # To maximize the number of substrings of all 0's, we need to minimize the number of 0's groups
        # So we distribute the 0's as evenly as possible between the m 1's
        
        # The number of 0's between the 1's is (n - m) // m, and some have one more
        # So the number of substrings of all 0's is sum of (k * (k + 1)) // 2 for each group of 0's
        # The maximum number of substrings of all 0's is when the 0's are as spread out as possible
        # So the number of 0's in each group is (n - m) // m or (n - m) // m + 1
        
        zeros_between = (n - m) // m
        extra_zeros = (n - m) % m
        
        # Number of substrings of all 0's
        substrings_of_zeros = 0
        for i in range(m):
            if i < extra_zeros:
                length = zeros_between + 1
            else:
                length = zeros_between
            substrings_of_zeros += length * (length + 1) // 2
        
        results.append(total_substrings - substrings_of_zeros)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()