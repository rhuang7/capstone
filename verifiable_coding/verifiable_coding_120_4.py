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
        
        # The maximum f(s) is achieved when the 1s are spread out as much as possible
        # So we calculate the number of substrings that contain at least one 1
        # Total possible substrings is n*(n+1)//2
        # Subtract the number of substrings that contain no 1s (i.e., all 0s)
        # The number of all 0s substrings is (k*(k+1))//2 where k is the number of 0s blocks
        # To maximize f(s), we should minimize the number of 0s blocks
        # So the optimal arrangement is to place 1s as spread out as possible
        
        # The number of 0s blocks is m + 1 (if 1s are placed with at least one 0 between them)
        # But if there are more 0s than that, we have to group them
        # So the number of 0s blocks is min(m + 1, n - m)
        
        k = n - m
        blocks = min(m + 1, k)
        
        # Number of all 0s substrings is sum of (length of each 0 block) * (length + 1) // 2
        # The optimal arrangement is to have the 0s as evenly distributed as possible
        # So each 0 block has either floor(k / blocks) or ceil(k / blocks) 0s
        # The total number of all 0s substrings is (k * (k + 1)) // 2
        # Because the 0s are grouped into blocks, but the total number of substrings of all 0s is the same as if they were all together
        
        all_zeros_substrings = (k * (k + 1)) // 2
        
        total_substrings = n * (n + 1) // 2
        result = total_substrings - all_zeros_substrings
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()