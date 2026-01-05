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
        
        # Maximum f(s) is achieved when 1's are spread as much as possible
        # So, we calculate the number of substrings that contain at least one '1'
        # Total possible substrings is n*(n+1)//2
        # Subtract the number of substrings that contain only '0's
        # The number of '0's is n - m
        # The number of substrings of all 0's is (n - m) * (n - m + 1) // 2
        total_substrings = n * (n + 1) // 2
        zero_substrings = (n - m) * (n - m + 1) // 2
        results.append(total_substrings - zero_substrings)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()