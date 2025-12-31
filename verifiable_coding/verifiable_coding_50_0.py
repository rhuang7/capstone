import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        
        total_s = a.count(1)
        total_b = a.count(2)
        
        # The total number of jars is 2n
        # We need to leave equal number of s and b jars
        # So the number of jars to be eaten is (total_s + total_b) - 2 * left
        # We need to find the maximum possible left such that left <= min(total_s, total_b)
        
        max_left = min(total_s, total_b)
        # We need to find the maximum possible left such that there exists a way to remove (total_s - left) s and (total_b - left) b jars
        
        # We can use a two-pointer approach to find the maximum left
        left = 0
        right = 0
        s_count = 0
        b_count = 0
        
        while left < 2 * n and right < 2 * n:
            if a[left] == 1:
                s_count += 1
            else:
                b_count += 1
            
            if s_count == b_count:
                left += 1
                right = left
            else:
                right += 1
        
        max_left = min(s_count, b_count)
        
        # The minimum number of jars to empty is (total_s + total_b) - 2 * max_left
        res = (total_s + total_b) - 2 * max_left
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()