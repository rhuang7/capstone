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
        
        ans = [0] * n
        
        # For each m from 1 to n, check if there exists a subarray that is a permutation of 1..m
        # We can track the positions of each number
        pos = [0] * (n + 1)
        for i in range(n):
            pos[p[i]] = i
        
        # For each m, check if the maximum position in 1..m is exactly m-1
        # This ensures that the subarray from 1 to max_pos is a permutation of 1..m
        max_pos = 0
        for m in range(1, n + 1):
            max_pos = max(max_pos, pos[m])
            if max_pos == m - 1:
                ans[m - 1] = 1
        
        results.append(''.join(map(str, ans)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()