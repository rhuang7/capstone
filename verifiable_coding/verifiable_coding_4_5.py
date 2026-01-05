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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        res = ['0'] * n
        
        # For each m from 1 to n, check if there exists a subarray that is a permutation of 1..m
        # We can track the positions of numbers 1..m and check if they form a contiguous block
        # We'll use a set to track the current numbers in the window
        # We'll also track the maximum value in the window
        
        # We'll iterate through the permutation and track the positions of numbers
        pos = [0] * (n + 1)  # pos[value] = index in permutation
        for i in range(n):
            pos[p[i]] = i
        
        # For each m, check if the positions of 1..m form a contiguous block
        # We can do this by checking if the maximum position of 1..m is equal to the minimum position of 1..m + m - 1
        # This is because if they form a contiguous block, the max position - min position + 1 = m
        
        for m in range(1, n + 1):
            min_pos = min(pos[i] for i in range(1, m + 1))
            max_pos = max(pos[i] for i in range(1, m + 1))
            if max_pos - min_pos + 1 == m:
                res[m - 1] = '1'
        
        results.append(''.join(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()