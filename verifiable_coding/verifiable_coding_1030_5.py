import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    Q = int(data[0])
    index = 1
    
    for _ in range(Q):
        n = int(data[index])
        u = int(data[index+1])
        v = int(data[index+2])
        index += 3
        
        # Find the path from u to v
        path = []
        while u != v:
            if u < v:
                path.append('left')
                u = u * 2
            else:
                path.append('right')
                u = u // 2
        
        # Count the number of pairs (w, t) that have the same path
        # The path is unique for each pair (w, t), so we need to find how many (w, t) have the same path as (u, v)
        # The number of such pairs is 2^k, where k is the length of the path
        # But we need to ensure that w and t are within [1, n]
        k = len(path)
        ans = 1 << k  # 2^k
        
        # Check if the path is valid for the given n
        # The path is valid if the path from u to v is entirely within the first n nodes
        # We need to check if the path from u to v is within the first n nodes
        # The path is valid if the path from u to v does not exceed n
        
        # The path from u to v is valid if the path from u to v is within the first n nodes
        # We can check this by simulating the path from u to v and ensuring that all nodes are <= n
        
        # Simulate the path from u to v
        w = u
        t = v
        for move in path:
            if move == 'left':
                w = w * 2
                t = t * 2
            else:
                w = w // 2
                t = t // 2
        
        # Check if w and t are within [1, n]
        if w > n or t > n:
            ans = 0
        
        print(ans)

if __name__ == '__main__':
    solve()