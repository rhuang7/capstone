import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    Q = int(data[0])
    idx = 1
    
    for _ in range(Q):
        n = int(data[idx])
        u = int(data[idx+1])
        v = int(data[idx+2])
        idx += 3
        
        # Function to get the path from u to v
        def get_path(u, v):
            path = []
            while u != v:
                if u < v:
                    path.append('left')
                    u = u * 2
                else:
                    path.append('right')
                    u = u // 2
            return path
        
        path = get_path(u, v)
        
        # Function to count number of pairs (w, t) with same path
        def count_pairs(n, path):
            if not path:
                return n * n
            cnt = 1
            for i in range(len(path)):
                if path[i] == 'left':
                    cnt *= 2
                else:
                    cnt *= 2
            return cnt
        
        ans = count_pairs(n, path)
        print(ans)

if __name__ == '__main__':
    solve()