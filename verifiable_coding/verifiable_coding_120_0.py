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
        
        # Maximum f(s) is achieved when 1s are spread out as much as possible
        # So, we calculate the number of substrings that contain at least one 1
        # Total number of substrings is n*(n+1)//2
        # Number of substrings with no 1s is (k)*(k+1)//2 where k is the number of 0s blocks
        # But since 1s are spread out, the 0s are in blocks of size 1
        # So, number of 0 blocks is m, and each block contributes (1*2)//2 = 1
        # So total substrings with no 1s is m
        # So answer is total substrings - m
        total_substrings = n * (n + 1) // 2
        results.append(total_substrings - m)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()